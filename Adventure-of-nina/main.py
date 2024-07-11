### Author - Chekuri Viroopaksh

import time
import json
import sys
import os
from helper import *
import datetime as dt

class GameLevel:
    def __init__(self,level=None):
        self.level = level
    
    def level1stage1(direction):
        if direction == 'west':
            pass
        
        else:
            pass

    def level1stage2():
        pass

# See the links in the Personal Brave for text based RPGs

commands = ["exit","help","save","menu","pause"]
definitions = {"exit":"Use this command to exit the game","help":"Use this command to get the help menu","save":"Use this command to save the current game state","menu":"Use this command to get to the main menu.","pause":"Use this command to get to the pause menu while in the game."}
current_game_config = {}

def unload_datetime(datetime):
    return dt.datetime.strptime(datetime,"%m/%d/%Y, %H:%M:%S")

def start_new():
    global current_game_config
    username = ""
    
    while True:
        if 3<=len(username)<=12:
            suitable = True
            for ch in username.lower():
                if not(ch in "*@abcdefghijklmnopqrstuvwxyz1234567890"):
                    suitable=False
                    break
            if suitable:
                break
            print("Invalid username.\n")
        else:
            username = input("What is your name?\n(At least 3 and at most 12 characters, cannot contain special characters except *,@)\n>> ")

    print("Hello "+username,end=", ")
    
    if (username+".json") in os.listdir():
        inp = input_handler("You already have a saved game. Do you want to start new?\n1)Yes\n2)No\n>> ",list("12"))
        if inp =='2':
            load_game(username)
    
    userage = input_handler("\nWhat is your age?\n>> ",[str(i) for i in range(3,101)],"Invalid age. Age must be 3 to 101.")

    current_game_config["username"] = username
    current_game_config['userage'] = userage
    current_game_config["actions"] = []
    current_game_config["states"] = []
    current_game_config['timestamp'] = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def load_game(username=""):
    f = 0
    global current_game_config
    while True:
        if not(username):
            inp = input("\nWhat's your username?\n>> ")
        else:
            inp = username
        if (inp+'.json') in os.listdir():
            print("\nWoohoo! Found your last saved game!!")
            current_game_config = json.loads(open(inp+'.json').read())
        else:
            f = 1
            print("Sorryy! We couldn't find your game. Are you sure?\n")
            out = input_handler("Do you want to go back to main menu?\n1) Yes\n2) No\n>> ",list("12"))
            if out == '1':
                break
        if not f:
            break

def help():
    global commands
    global definitions
    helper_func(commands,definitions)

def save_game():
    # Use JSON files for saving the game
    f = open(current_game_config['username']+'.json','w')
    current_game_config["timestamp"] = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    f.write(json.dumps(current_game_config))
    print("Game saved!")

def exit_game():
    # Handle saving the game etc. before exiting
    user_input = input_handler("Do you want to save the game?\n1. Yes\n2. No\n>> ",list("12"),"")
    if user_input=='1':
        save_game()
    sys.exit(0)

def menu(inp,state='start'):
    if state=='start':
        if inp == '1':
            start_new()
        elif inp == '2':
            load_game()
        elif inp == '3':
            help()
        elif inp == '4':
            about_me()
        else:
            exit_game()
    else:
        if inp == '1':
            return "resume"
        elif inp == '2':
            return "menu"
        elif inp == '3':
            help()
        elif inp == '4':
            about_me()
        else:
            exit_game()

def get_level(states,actions):
    pass

def progress(level,stage,states,actions):
    pass

def play():
    global commands
    global current_game_config
    global definitions
    welcome()
    while True:
        inp = home_screen(state='start')
        while True:
            menu(inp,'start')
            if inp in '12':
                if inp == '1' or (inp == '2' and current_game_config):
                    break
                
            inp = home_screen(state='start')

        inp = input("Do you want to start playing?\n1) Yes\n2) No\n>> ")
        
        game_play = False
        if inp=='1':
            game_play = True
            started = True
            print("Maximize your console for immersive experience!")
        else:
            continue

        states,actions = current_game_config['states'],current_game_config['actions']
        while True:
            # Inner loop for playing the actual game
            if game_play:
                if started:
                    game_opening()
                    started = False
                    level,stage = get_level(states,actions)

                progress(level,stage,states,actions)

                print("What do you want to do?")
                option = input(">> ")
                if option in commands:
                    if option == 'pause':
                        inp = home_screen('pause')
                        output = menu(inp,'pause')
                        if output == 'menu':
                            game_play = False
                        else:
                            continue
                    elif option == 'menu':
                        game_play = False
                    elif option == 'help':
                        help()
                    elif option == 'exit':
                        exit_game()
                    elif option =='save':
                        save_game()
                else:
                    print(f"{option} command not found! Use help for available commands.\n")
                # Starting a new game
                
            else:
                inp = home_screen(state='pause')
                menu(inp)
                pass 
            
            if game_play==False:
                break

while __name__ == "__main__":
    play()