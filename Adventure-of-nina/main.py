### Author - Chekuri Viroopaksh

import time
import sys
from helper import *

# See the links in the Personal Brave for text based RPGs

commands = []
definitions = {}
current_game_config = {}

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
        

def load_game():
    
    pass

def help():
    global commands
    global definitions
    print(f"""
{f'{"`"*135}'}

                The available commands are:""")
    for command in commands:
        print(f"{command} - {definitions[command]}")
        time.sleep(1)
    print()
    time.sleep(5)

def save_game(states):
    # Use JSON files for saving the game
    pass

def exit_game(states):
    # Handle saving the game etc. before exiting
    user_input = ""
    while True:
        if user_input in list("12"):
            break
        user_input = input("Do you want to save the game?\n1. Yes\n2. No\n>> ")
    if user_input=='1':
        save_game(states)
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

        if inp=='2':
            current_game_config,game_play = load_game()
        else:
            game_play = []

        while True:
            # Inner loop for playing the actual game
            if not game_play:
                game_opening()
                print("What do you want to do?")
                option = input(">> ")
                if option == 'exit':
                    print("Thanks for playing the game.")
                    sys.exit(0)
                # Starting a new game

            else:
                # Continue a game from previous saved point.
                pass 
            pass

while __name__ == "__main__":
    play()