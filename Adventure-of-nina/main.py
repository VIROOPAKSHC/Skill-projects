import tkinter as tk
from tkinter import scrolledtext
import sys
class TextAdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventures of Nina")
        self.root.configure(bg='black')
        self.root.geometry("500x500")
        self.state = []
        self.state.append("Process Created")
        # Creating text display area
        self.text_area = scrolledtext.ScrolledText(self.root,bg='black',fg='white', wrap=tk.WORD, width=60, height=20, font=("Times New Roman", 14))
        self.text_area.pack(pady=10)
        self.text_area.insert(tk.END, self.welcome_message())
        
        # Creating input field
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        self.input_field = tk.Entry(self.input_frame, width=50, font=("Times New Roman", 12))
        self.input_field.pack(side=tk.LEFT, padx=10)
        self.input_field.bind("<Return>", self.process_input)

        # Submit button
        self.submit_button = tk.Button(self.input_frame,bg='black',fg='white',text="Submit", command=self.process_input)
        self.submit_button.pack(side=tk.RIGHT)

    def welcome_message(self):
        self.state.append("Welcome Screen")
        return """
Welcome to Adventures of Nina!!! 
Press Enter to start!
            """

    def handle_input(self,user_input):
        if user_input == '1':
            self.state.append("New Game")
            self.start_new_game()
        elif user_input == '2':
            self.load_game()
            self.state.append("Load Game")
        elif user_input=='3':
            self.state.append("Help")
            self.show_help()
        elif user_input=='4':
            self.state.append("About Me")
            self.about_me()
        else:
            self.text_area.insert(tk.END,"Do you want to save the game?\n 1. Yes\n2. No")
            self.state.append('Save state')
            

    def menu(self):
        if self.state[-1]=='Entering Game':
            self.state.append('Menu')
            self.text_area.insert(tk.END,"""\n
            Enter a number from the following
1. New Game
2. Load Game
3. Help
4. About Me
5. Exit
""")
            self.input_field.delete(0, tk.END)
        else:
            self.text_area.insert(tk.END,"""\n
            Enter a number from the following
1. Continue Game
2. New Game
3. Help
4. About Me
5. Exit
""")
            user_input = self.input_field.get()
            self.input_field.delete(0, tk.END)

    def process_input(self, event=None):
        
        user_input = self.input_field.get()
        if self.state[-1] == 'Welcome Screen':
            self.state.append("Entering Game")
            self.menu()
        elif self.state[-1] == 'Menu':
            if not (user_input in list("12345")):
                self.text_area.insert(tk.END,'\nEnter valid option')
                self.menu()
            else:
                self.input_field.delete(0,tk.END)
                self.handle_input(user_input)
        elif self.state[-1] == 'Save state':
            if user_input=='1':
                self.save_game()
            sys.exit(0)
        else:
            self.text_area.insert(tk.END, f"\n> {user_input}\n")
            self.input_field.delete(0, tk.END)

        # Process the input and generate a response
            response = self.generate_response(user_input)
            self.text_area.insert(tk.END, f"{response}\n")
        
        self.text_area.yview(tk.END)  # Scroll to the bottom
        

    def generate_response(self, user_input):
        # Handle the game logic here and return the response string
        # This is a placeholder for the actual game logic
        return "You chose: " + user_input

if __name__ == "__main__":
    root = tk.Tk()
    game = TextAdventureGame(root)
    root.mainloop()