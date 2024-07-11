### Author - Chekuri Viroopaksh

import time
import json
import sys
import os
from helper import *
import datetime as dt


# See the links in the Personal Brave for text based RPGs

commands = ["exit","help","save","menu"]
definitions = {"exit":"Use this command to exit the game","help":"Use this command to get the help menu","save":"Use this command to save the current game state","menu":"Use this command to get to the main menu."}
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
            username = input("              What is your name?\n(At least 3 and at most 12 characters, cannot contain special characters except *,@)\n>> ")
    print("Hello "+username,end=", ")
    if (username+".json") in os.listdir():
        print("You already have a saved game. Do you want to start new?\n1)Yes\n2)No\n")
        inp = input(">> ")
        while not(inp in "12"):
            inp = input("Enter a valid option.\n1)Start new.\n2)Continue from saved.\n>> ")
        if inp =='2':
            load_game(username)
    userage = -1
    while True:
        if 3 <= userage <= 100:
            break
        else:
            userage = input("What is your age?\n>> ")
            try:
                userage = int(userage)
            except:
                userage = -1
                print("Invalid age.\n")

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
            inp = input("What's your username?\n>> ")
        else:
            inp = username
        if (inp+'.json') in os.listdir():
            print("Woohoo! Found your last saved game!!")
            current_game_config = json.loads(open(inp+'.json').read())
        else:
            f = 1
            print("Sorryy! We couldn't find your game. Are you sure?")
        
        if not f:
            break

def help():
    global commands
    global definitions

    print(f"""
{f'{"`"*135}'}

The available commands are:\n\n""")
    for command in commands:
        print(f"{command} - {definitions[command]}")
        time.sleep(1)
    print()
    time.sleep(5)
    print(f"""
{f'{"`"*135}'}\n""")

def save_game():
    # Use JSON files for saving the game
    f = open(current_game_config['username']+'.json','w')
    current_game_config["timestamp"] = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    f.write(json.dumps(current_game_config))
    print("Game saved!")


def exit_game(states):
    # Handle saving the game etc. before exiting
    user_input = ""
    while True:
        if user_input in list("12"):
            break
        user_input = input("Do you want to save the game?\n1. Yes\n2. No\n>> ")
    if user_input=='1':
        save_game()
    sys.exit(0)

def menu(states,inp):
    if inp == '1':
        states.append("Start New")
        start_new()
    elif inp == '2':
        states.append("Load")
        load_game()
    elif inp == '3':
        states.append("Help")
        help()
    elif inp == '4':
        states.append("About Me")
        about_me()
    else:
        states.append("Exit")
        exit_game(states)


def play():
    global commands
    global current_game_config
    global definitions

    states = []
    welcome(states)
    
    while True:
        inp = home_screen(states,state='start')
        if states[-1] == 'Start Screen':
            while True:
                menu(states,inp)
                if inp in '12':
                    break
                inp = home_screen(states,state='start')

        inp = input("Do you want to start playing?\n1) Yes\n2) No\n>> ")
        if inp=='1':
            game_play = True
            started = False
            print("Maximize your console for immersive experience!")
        else:
            continue
        while True:
            # Inner loop for playing the actual game
            if game_play:
                if not started:
                    game_opening()
                    started = True
                print("What do you want to do?")
                option = input(">> ")
                if option in commands:
                    if option == 'menu':
                        game_play = False
                    elif option == 'help':
                        states.append("Help")
                        help()
                    elif option == 'exit':
                        states.append("Exit")
                        exit_game(states)
                    else:
                        save_game()
                else:
                    print(f"{option} command not found! Use help for available commands.\n")
                # Starting a new game
                
            else:
                # Continue a game from previous saved point.
                inp = home_screen(states)
                menu(states,inp)
                pass 
            pass

while __name__ == "__main__":
    play()