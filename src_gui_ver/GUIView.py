from tkinter import *
import tkinter as tk

class View(tk.Tk):
        
    ROLES = ["Member", "Trainer", "Admin"]
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("DatabaseApp")
        self.geometry("350x350")
        self.mainframe = None
        
        self._create_start_screen()
        
    def main(self):    
        self.mainloop()
    
    def _create_start_screen(self):
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(padx=5, pady=5)
        
        title = Label(self.mainframe, text="Database Management System", font=('Arial', 18))
        title.pack()
        prompt = Label(self.mainframe, text="Pick a role from the options below", font=('Arial', 12))
        prompt.pack()
        self._create_options()

    def _create_options(self):
        frame = tk.Frame(self.mainframe)
        frame.pack()
        
        for option in self.ROLES:
            button = tk.Button(frame, text=option, font=("Arial", 10))
            button.pack(side="left")