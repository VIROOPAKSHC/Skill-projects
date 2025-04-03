import copy
import random
import numpy as np

from game import Game, states

HIT = 0
STAND = 1
DISCOUNT = 0.95 

class Agent:
    def __init__(self):

        self.MC_values = {} # Dictionary: Store the MC value of each state
        self.S_MC = {}      # Dictionary: Store the sum of returns in each state
        self.N_MC = {}      # Dictionary: Store the number of samples of each state


        self.TD_values = {}  # Dictionary: Store the TD value of each state
        self.N_TD = {}       # Dictionary: Store the number of samples of each state

        self.Q_values = {}   # Dictionary: Store the Q-Learning value of each state and action
        self.N_Q = {}        # Dictionary: Store the number of samples of each state for each action

        for s in states:
            self.MC_values[s] = 0
            self.S_MC[s] = 0
            self.N_MC[s] = 0
            self.TD_values[s] = 0
            self.N_TD[s] = 0
            self.Q_values[s] = [0,0] # First element is the Q value of "Hit", second element is the Q value of "Stand"
            self.N_Q[s] = [0,0] # First element is the number of visits of "Hit" at state s, second element is the number of visits of "Stand" at s

        self.simulator = Game()

    @staticmethod
    def default_policy(state):
        user_sum = state[0]
        user_A_active = state[1]
        actual_user_sum = user_sum + user_A_active * 10
        if actual_user_sum < 14:
            return 0
        else:
            return 1

    @staticmethod
    def alpha(n):
        return 10.0/(9 + n)
   
    def make_one_transition(self, action):
        if self.simulator.game_over():
            return None

        if action==0:
            self.simulator.act_hit()
            return self.simulator.state
        else:
            self.simulator.act_stand()
            return self.simulator.state
        

    def MC_run(self, num_simulation, tester=False):

        for simulation in range(num_simulation):

            if tester:
                self.tester_print(simulation, num_simulation, "MC")
            self.simulator.reset()  

            episode = []
            while not self.simulator.game_over():
                state = self.simulator.state
                action = self.default_policy(state)
                self.make_one_transition(action)
                
                new_state = self.simulator.state
                episode.append([state,action,0,new_state])

                if self.simulator.game_over() and self.simulator.check_reward():
                    reward = self.simulator.check_reward()
                    episode.append([new_state,None,reward,None])
            
            for i in range(len(episode)):
                state,action,reward,new_state = episode[i]
                self.N_MC[state]+=1
                cumulative_reward = 0
                for epi in episode[i:][::-1]:
                    cumulative_reward = DISCOUNT*cumulative_reward+epi[2]
                self.S_MC[state]+=cumulative_reward
                self.MC_values[state]=self.S_MC[state]/self.N_MC[state]
            


    def TD_run(self, num_simulation, tester=False):

        for simulation in range(num_simulation):

            if tester:
                self.tester_print(simulation, num_simulation, "TD")
            self.simulator.reset()

            while not self.simulator.game_over():
                state = self.simulator.state
                action = self.default_policy(state)
                self.make_one_transition(action)
                new_state = self.simulator.state
                self.N_TD[state]+=1

                if self.simulator.game_over():
                    self.TD_values[state] = self.TD_values[state] + self.alpha(self.N_TD[state])*(0+DISCOUNT*self.TD_values[new_state]-self.TD_values[state])
                    self.N_TD[new_state]+=1
                    reward = self.simulator.check_reward()
                    self.TD_values[new_state] = self.TD_values[new_state] + self.alpha(self.N_TD[new_state])*(reward-self.TD_values[new_state])
                else:
                    self.TD_values[state] = self.TD_values[state] + self.alpha(self.N_TD[state])*(0+DISCOUNT*self.TD_values[new_state]-self.TD_values[state])

                
    def Q_run(self, num_simulation, tester=False, epsilon=0.4):

        for simulation in range(num_simulation):

            if tester:
                self.tester_print(simulation, num_simulation, "Q")
            self.simulator.reset()

            while not self.simulator.game_over():
                state = self.simulator.state
                action = self.pick_action(state,epsilon)
                self.make_one_transition(action)
                self.N_Q[state][action]+=1
                new_state = self.simulator.state
                reward = self.simulator.check_reward()
                self.Q_values[state][action] = self.Q_values[state][action] + self.alpha(self.N_Q[state][action])*(reward+DISCOUNT*np.max(self.Q_values[new_state])-self.Q_values[state][action])


    def pick_action(self, s, epsilon):
        
        if np.random.rand() < epsilon:
            return np.random.randint(0,2)
        else:
            return np.argmax(self.Q_values[s])


    def autoplay_decision(self, state):
        hitQ, standQ = self.Q_values[state][HIT], self.Q_values[state][STAND]
        if hitQ > standQ:
            return HIT
        if standQ > hitQ:
            return STAND
        return HIT 

    def save(self, filename):
        with open(filename, "w") as file:
            for table in [self.MC_values, self.TD_values, self.Q_values, self.S_MC, self.N_MC, self.N_TD, self.N_Q]:
                for key in table:
                    key_str = str(key).replace(" ", "")
                    entry_str = str(table[key]).replace(" ", "")
                    file.write(f"{key_str} {entry_str}\n")
                file.write("\n")

    def load(self, filename):
        with open(filename) as file:
            text = file.read()
            MC_values_text, TD_values_text, Q_values_text, S_MC_text, N_MC_text, NTD_text, NQ_text, _  = text.split("\n\n")
            
            def extract_key(key_str):
                return tuple([int(x) for x in key_str[1:-1].split(",")])
            
            for table, text in zip(
                [self.MC_values, self.TD_values, self.Q_values, self.S_MC, self.N_MC, self.N_TD, self.N_Q], 
                [MC_values_text, TD_values_text, Q_values_text, S_MC_text, N_MC_text, NTD_text, NQ_text]
            ):
                for line in text.split("\n"):
                    key_str, entry_str = line.split(" ")
                    key = extract_key(key_str)
                    table[key] = eval(entry_str)

    @staticmethod
    def tester_print(i, n, name):
        print(f"\r  {name} {i + 1}/{n}", end="")
        if i == n - 1:
            print()
