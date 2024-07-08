import time
import sys

commands = []
definitions = {}
current_game_config = {}


def welcome(states):

    states.append("Welcome Screen")
    print(f"""
{f'{"`"*135}'}

          
                                            Welcome to the Adventures of Nina


{f'{"`"*135}'}
""")
    time.sleep(2)
    

def game_opening():
    s = (f"""Many Many years earlier in the year 5352 BC, the world was full of trees and wildlife. Earth thrived with resources and abundance of
freshness. Humans co-lived with animals, not in the form of pets but as family members, they enjoyed the world together and believed
respect and love is the ultimate way to reach eternal happiness. Everyone knew their way to the soul. Towards the north of the 
Himalayan mountains, people lived in a village called Hustin who were protected by a tribe named Arzuns with special abilities to 
harness the power of their soul through magic and archery. Towards the west of the mountains, there was another village called Kara
protected by the tribe named Darodans, who also possessed special abilities but through mystic sorcery and maces. Together, 
they protected their tribes from the Gundarvas in the abandoned forest located near the Himalayas and in between the tribes. 
Both the tribes enjoyed together in a religious festival every year the 3rd week of Monsoon.
""")
    print(f"{'-'*150}\n{'-'*150}\n{'-'*150}\n{'-'*150}\n")
    for line in s.split("\n"):
        time.sleep(3)
        print(" "*16,end="")
        for word in line.split():
            print(word,end=" ")
        print("\n",end="")
        
    time.sleep(4)

    s = ("""Everything went fine, until one day the villagers of the North noticed people missing from their homes. Alarmed, everyone reached out
to the Village head. The village head seeked the help of Arzuns in this matter. Women from this tribe, have powers to understand the
situation using magic and the particles of the air. When sought for help, their women told the village, a peculiar creature seems to
be coming to their village by the night and somehow making people vanish. They doubted the Gundarvas in the forest to be the culprits
for their situation. After deciding, the village head decided to send their strongest soldier Nina to the forest to speak, if required
slay the Gundarvas of the forest. 
""")
    print(f"{'-'*150}\n{'-'*150}\n{'-'*150}\n{'-'*150}\n")
    for line in s.split("\n"):
        time.sleep(3)
        print(" "*16,end="")
        for word in line.split():
            print(word,end=" ")
        print("\n",end="")
    
        
    print(f"{'-'*135}")
    time.sleep(4)
    



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
            username = input("              What is your name?\n(At least 3 and at most 12 characters, cannot contain special characters except *,@)\n>>")
    
    userage = -1
    while True:
        if 3 <= userage <= 100:
            break
        else:
            userage = input("               What is your age?\n>")
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
    print(f"""{f'{"`"*135}'}
""")
    time.sleep(5)
    

def about_me():
    print(f"""
{f'{"-"*135}'}

                Hi! I am the developer of this game. I am Chekuri Viroopaksh.
                Somethings about me:
                    I am interested in programming in general, Artificial Intelligence,
                    books and some other things.
                If you would like to connect with me, check on linkedin at
                linkedin.com/viroopaksh-chekuri
                My Github accout is, github.com/VIROOPAKSHC
                Have fun!!

{f'{"-"*135}'}
""")
    time.sleep(3)

def save_game(states):
    # Use JSON files for saving the game
    pass

def exit_game(states):
    # Handle saving the game etc. before exiting
    user_input = ""
    while True:
        if user_input in list("12"):
            break
        user_input = input("Do you want to save the game?\n1. Yes\n2. No\n>")
    if user_input=='1':
        save_game(states)
    sys.exit(0)

def home_screen(states,state='start'):
    if state=='start':
        states.append("Start Screen")
        inp = ""
        while True:
            print(f"""
{f'{"`"*135}'}

                Select a number from the following
                1) New Game
                2) Load Game
                3) Help
                4) About Me
                5) Exit


{f'{"`"*135}'}\n
    """)
            inp = input(">")
            if (inp in list("12345")):
                break

        return inp

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
                # Starting a new game

            else:
                # Continue a game from previous saved point.
                pass 
            pass
# play()
game_opening()