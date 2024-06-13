import time
import sys

# line_break = "-"*500
def print_welcome():
    l = ("""
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
    Welcome!!!
This is a text-based adventure game developed alone by Viroopaksh Chekuri.
Please maximize your command prompt for better experience.
You can find his projects at github.com\VIROOPAKSHC.
Please feel free to reach out for any issues in the game.
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)

def opening_instructions():
    l = ("""
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
This is version 1.0 of the game.
Follow the commands available to progress in the game.
You can find all the available commands using the \h option. 
After every session, you would be given an option to save the game, 
if you have played for longer it might be needed for a little longer to store.
Please do not force exit while saving the game.
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)

def Print():
    print()
    print()

def instructions():
    Print()
    l = ("""
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
This game is a single player adventure.
A player can choose his quest, dialogue, action or path along the game solely by his actions throughout the game.
Nina encounters several hurdles throughout her path and learns who she is, and what she is destined to do.
Remember, the course of the game might change as you choose the actions and path and might cause you to lose.
The game shall give you an option to come back to the last checkpoint if you lost to continue again and continue making right choices.
However, there is not a single right permutation of actions you should take to reach the goal. 
---------------------------------------------------------------------------------------------------------------------------------------         
---------------------------------------------------------------------------------------------------------------------------------------
""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)
    
    print("""
Wish you all the best. Enjoy!!!
          - Message from the Developer
""")
    Print()

def StartNewGame():
    name = input("Provide name under which the game is to be saved: ")
    while not(name):
        name = input("Provide name under which the game is to be saved: ")
    l = ("""
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
Centuries ahead, In the year 3640.
A girl named Nina wakes up in a small near-dismantled house in a warrior attire.
She finds herself stuck in a room. Nina does not remember anything before today only glimpses of some images through her dreams.
These dreams seem to be real but might have been illusions of the future or past.

Find a way out!.
----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)

def main():
    sys.stdout.flush()
    print_welcome()
    time.sleep(1)
    Print()
    sys.stdout.flush()
    opening_instructions()
    print("Choose an option from the Menu")
    option = input("""
1. Start a New Game
2. Load Saved Game
3. Instructions
4. Help
5. Exit                  
> """)
    while True:
        if '1'<=option<='5':
            break
        option = input("""
1. Start a New Game
2. Load Saved Game
3. Instructions
4. Help
5. Exit                      
> """)
    match option:
        case '1': 
            StartNewGame()
        case '2': 
            LoadGame()
        case '3': 
            instructions()
        case '4': 
            help()
        case '5':
            exit()
        case default: pass
    while True:
        inp = input("> ")
        if inp == '\h':
            Print()
            instructions()
            Print()
        elif inp == 'exit':
            Print()
            print("Do you really want to exit the game? Y/N")
            inp = input("> ")
            if inp=='Y':
                Print()
                print("Thanks for playing the game.")
                break
        else:
            Print()
            print("Invalid command please try another command or use \h.")
    Print()

if  __name__ == "__main__":
    main()