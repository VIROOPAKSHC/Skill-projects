import time
import sys

line_break = "-"*500
def print_welcome():
    l = ("""This is a text-based adventure game developed alone by Viroopaksh Chekuri.
You can find his projects at github.com\VIROOPAKSHC.
Please feel free to reach out for any issues in the game.""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)

def instructions():
    l = ("""This is version 1.0 of the game.
Follow the commands available to progress in the game.
You can find all the available commands using the \h option. 
After every session, you would be given an option to save the game, 
if you have played for longer it might be needed for a little longer to store.
Please do not force exit while saving the game.""").split("\n")
    for line in l:
        print(line)
        time.sleep(2)

def Print():
    print()
    print()

def main():
    sys.stdout.flush()
    print_welcome()
    time.sleep(1)
    Print()
    print(line_break)
    Print()
    sys.stdout.flush()
    instructions()
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