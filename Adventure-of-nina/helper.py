import time

def input_handler(message: str,options: list,error_message = ''):
    inp = ""
    while True:
        inp = input(message)
        if inp in options:
            return inp
        if not error_message:
            print(f"No available command. Select from {options}")
        else:
            print(error_message)

def helper_func(comms,defs):
    
    print(f"""
{f'{"`"*135}'}

The available commands are:\n\n""")
    for command in comms:
        print(f"{command} - {defs[command]}")
        time.sleep(1)
    print()
    time.sleep(5)
    print(f"""
{f'{"`"*135}'}\n""")
    
def welcome():

    print(f"""
{f'{"`"*135}'}

          
                                            WELCOME TO THE ADVENTURES OF NINA!
                                        This game is brought to you by BlackMoonBear Studios


{f'{"`"*135}'}\n""")
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
    print(f"{'`'*135}\n{'`'*135}\n")
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
    print(f"{'`'*135}\n{'`'*135}\n")
    for line in s.split("\n"):
        time.sleep(3)
        print(" "*16,end="")
        for word in line.split():
            print(word,end=" ")
        print("\n",end="")
    
        
    print(f"{'-'*135}")
    time.sleep(4)

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

def home_screen(state='start'):
    if state=='start':
        inp = input_handler("""

            Select a number from the following
            1) New Game
            2) Load Game
            3) Help
            4) About Me
            5) Exit


>> """,list("12345"))
    elif state=='pause':
        inp = input_handler("""

            Select a number from the following
            1) Resume Game
            2) Main Menu
            3) Help
            4) About Me
            5) Exit


>> """,list("12345"))
    return inp
