import tkinter as tk
from tkinter import Label, Button
import time

#Displaying login time to the user
localtime = time.asctime(time.localtime(time.time()))

class App1:
    def __init__(self, top):
        self.top = top  #name of the window
        top.title("Restaurant Manager")
        top.geometry("1028x500")
        top.configure(bg="#091833") #Dark blue colour

        #Creating variables for fonts for easy accessibility
        font_1 = "{Courier New} 10 normal" 
        font_2 = "{U.S. 101} 30 bold"
        font_3 = "{Al-Aramco} 11 bold"
        font_4 = "{Courier New} 10 bold"
        font_5 = "{Segoe UI} 15 bold"
        font_6 = "Ariel 13 bold"
        font_7 = "{Segoe UI} 13 bold" 
        font_8 = "{Times New Roman}, 12 normal"

        #----------- Food Info-----------#

        self.TitleHeader = tk.Label(master=top, text="RESTAURANT MANAGER", bg="#091833", font=font_2, fg="#f2a343")
        self.TitleHeader.place(relx = 0.268, rely=0.02, height=51, width=507) 

        #Creating label to harbour and display time. Login time doesn't change  
        localtime1 = Label(master=top, text=localtime, bg="#091833", font=font_1, fg="steel blue")
        localtime1.place(relx = 0.420, rely=0.12)  

        #----------- Food Label-----------#
        self.LabelOrder = tk.Label(master=top, text="Order Num :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.25)
        self.LabelOrder = tk.Label(master=top, text="Jollof Rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.32)
        self.LabelOrder = tk.Label(master=top, text="Fried rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.4)
        self.LabelOrder = tk.Label(master=top, text="Banku & tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.48)
        self.LabelOrder = tk.Label(master=top, text="Fufu & mutton soup :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.56)
        self.LabelOrder = tk.Label(master=top, text="Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.64)
        self.LabelOrder = tk.Label(master=top, text="Drinks :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.054, rely=0.71)

        #----------- Food Label-----------#
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.25)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.32)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.4)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.48)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.56)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.64)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.25, rely=0.71)

'''Making a main root so that the window will not disappear once the program is run'''
root = tk.Tk()
my_gui = App1(root)
root.mainloop()