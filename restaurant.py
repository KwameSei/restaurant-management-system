from logging import root
import tkinter as tk

class App1:
    def __init__(self, top):
        self.top = top  #name of the window
        top.title("Restaurant Manager")
        top.geometry("1028x500")
        top.configure(bg="#091833") #Dark blue colour

        #Creating variables for fonts for easy accessibility
        font10 = "{Courier New} 10 normal" 
        font11 = "{U.S. 101} 30 bold"
        font12 = "{Al-Aramco 11 bold}"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Ariel 13 bold"
        font16 = "{Segoe UI} 13 bold"       

'''Making a main root so that the window will not disappear once the program is run'''
root = tk.Tk()
my_gui = App1(root)
root.mainloop()