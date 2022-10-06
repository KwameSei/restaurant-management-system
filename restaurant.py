from logging import root
import tkinter as tk

class App1:
    def __init__(self, top):
        self.top = top  #name of the window
        top.title("Restaurant Manager")
        top.geometry("1028x500")
        top.configure(bg="#091833") #Dark blue colour

'''Making a main root so that the window will not disappear once the program is run'''
root = tk.Tk()
my_gui = App1(root)
root.mainloop()