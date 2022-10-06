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

        #----------- Creating builtin calculator-----------#
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.705, rely=0.24, height=35, relwidth=0.230)
        
        self.one_button = tk.Button(master=top, text='''1''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.one_button.place(relx=0.705, rely=0.34, height=50, width=50)
        self.two_button = tk.Button(master=top, text='''2''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.two_button.place(relx=0.765, rely=0.34, height=50, width=50)
        self.three_button = tk.Button(master=top, text='''3''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.three_button.place(relx=0.825, rely=0.34, height=50, width=50)
        
        self.four_button = tk.Button(master=top, text='''4''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.four_button.place(relx=0.705, rely=0.45, height=50, width=50)
        self.five_button = tk.Button(master=top, text='''5''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.five_button.place(relx=0.765, rely=0.45, height=50, width=50)
        self.six_button = tk.Button(master=top, text='''6''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.six_button.place(relx=0.825, rely=0.45, height=50, width=50)

        self.seven_button = tk.Button(master=top, text='''7''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.seven_button.place(relx=0.705, rely=0.56, height=50, width=50)
        self.eight_button = tk.Button(master=top, text='''8''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.eight_button.place(relx=0.765, rely=0.56, height=50, width=50)
        self.nine_button = tk.Button(master=top, text='''9''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.nine_button.place(relx=0.825, rely=0.56, height=50, width=50)

        self.zero_button = tk.Button(master=top, text='''0''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.zero_button.place(relx=0.765, rely=0.67, height=50, width=50)
        self.decimal_button = tk.Button(master=top, text='''.''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.decimal_button.place(relx=0.705, rely=0.67, height=50, width=50)
        self.mod_button = tk.Button(master=top, text='''%''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.mod_button.place(relx=0.825, rely=0.67, height=50, width=50)
        self.del_all_button = tk.Button(master=top, text='''C''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.del_all_button.place(relx=0.705, rely=0.78, height=50, width=50)
        self.del_one_button = tk.Button(master=top, text='''⌫''', bg='red', fg='#ffffff', font=font_5, borderwidth='1')
        self.del_one_button.place(relx=0.765, rely=0.78, height=50, width=50)

        self.add_button = tk.Button(master=top, text='''+''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.add_button.place(relx=0.885, rely=0.34, height=50, width=50)
        self.sub_button = tk.Button(master=top, text='''-''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.sub_button.place(relx=0.885, rely=0.45, height=50, width=50)
        self.mul_button = tk.Button(master=top, text='''*''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.mul_button.place(relx=0.885, rely=0.56, height=50, width=50)
        self.div_button = tk.Button(master=top, text='''/''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.div_button.place(relx=0.885, rely=0.67, height=50, width=50)
        self.equal_button = tk.Button(master=top, text='''=''', bg='green', fg='#ffffff', font=font_5, borderwidth='1')
        self.equal_button.place(relx=0.825, rely=0.78, height=50, width=113)

        #----------- List Food Cost-----------#
        self.LabelCost = tk.Label(master=top, text="Cost :", font=font_3, fg='red', bg='#091833')
        self.LabelCost.place(relx=0.46, rely=0.32)
        self.Label_service = tk.Label(master=top, text="Service Charge :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_service.place(relx=0.43, rely=0.4)
        self.Label_tax = tk.Label(master=top, text="Tax :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_tax.place(relx=0.46, rely=0.48)
        self.Label_subtotal = tk.Label(master=top, text="Subtotal :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_subtotal.place(relx=0.45, rely=0.56)
        self.Label_total = tk.Label(master=top, text="Total :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_total.place(relx=0.46, rely=0.64)


        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.56, rely=0.32, relwidth=0.111)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.56, rely=0.4, relwidth=0.111)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.56, rely=0.48, relwidth=0.111)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.56, rely=0.56, relwidth=0.111)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.56, rely=0.64, relwidth=0.111)
        

'''Making a main root so that the window will not disappear once the program is run'''
root = tk.Tk()
my_gui = App1(root)
root.mainloop()