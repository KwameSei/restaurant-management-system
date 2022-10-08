from cgitb import text
import tkinter as tk
from tkinter import DISABLED, END, Checkbutton, Label, Button, IntVar, StringVar
import time
import parser

#Displaying login time to the user
localtime = time.asctime(time.localtime(time.time()))

root = tk.Tk()  #name of the window
root.title("Restaurant Manager")
root.geometry("1270x690+0+0")
root.resizable(False, False)
root.configure(bg="#091833") #Dark blue colour

#Creating variables for fonts for easy accessibility
font_1 = "{Courier New} 10 normal" 
font_2 = "{U.S. 101} 30 bold"
font_3 = "{Al-Aramco} 11 bold"
font_4 = "{Courier New} 10 bold"
font_5 = "{Segoe UI} 15 bold"
font_6 = "Ariel 13 bold"
font_7 = "{Segoe UI} 13 bold" 
#font_8 = "{Times New Roman}, 12"

#Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var27 = IntVar()
var28 = IntVar()

food1 = StringVar()
food2 = StringVar()
food3 = StringVar()
food4 = StringVar()
food5 = StringVar()
food6 = StringVar()
food7 = StringVar()

#Costs entry
foodcostvar = StringVar()
drinkscostvar = StringVar()
costvar = StringVar()
taxvar = StringVar()
subtotalvar = StringVar()
totalvar = StringVar()

#Setting empty fields to zero
food1.set('0')
food2.set('0')
food3.set('0')
food4.set('0')
food5.set('0')
food6.set('0')
food7.set('0')

#----------- Food Info-----------#

TitleHeader = tk.Label(root, text="RESTAURANT MANAGER", bg="#091833", font=font_2, fg="#f2a343")
TitleHeader.place(relx = 0.268, rely=0.02, height=51, width=507) 

#Creating label to harbour and display time. Login time doesn't change  
localtime1 = Label(root, text=localtime, bg="#091833", font=font_1, fg="steel blue")
localtime1.place(relx = 0.420, rely=0.12)  

#----------- Food Label-----------#
LabelOrder = tk.Label(root, text="Order Num :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.25)
LabelOrder = tk.Label(root, text="Jollof Rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.32)
LabelOrder = tk.Label(root, text="Fried rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.4)
LabelOrder = tk.Label(root, text="Banku & tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.48)
LabelOrder = tk.Label(root, text="Fufu & mutton soup :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.56)
LabelOrder = tk.Label(root, text="Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.64)
LabelOrder = tk.Label(root, text="Drinks :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.71)

        #----------- Food Label-----------#
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food1, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.25)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food2, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.32)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food3, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.4)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food4, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.48)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food5, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.56)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food6, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.64)
entryOrder = tk.Entry(root, bg='#d9d9d9',state=DISABLED, textvariable=food7, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryOrder.place(relx=0.16, rely=0.71)

foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var1, background='#091833')
foodCheck.place(relx=0.004, rely=0.32)
foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var2, background='#091833')
foodCheck.place(relx=0.004, rely=0.4)
foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var3, background='#091833')
foodCheck.place(relx=0.004, rely=0.48)
foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var4, background='#091833')
foodCheck.place(relx=0.004, rely=0.56)
foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var5, background='#091833')
foodCheck.place(relx=0.004, rely=0.64)
foodCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var6, background='#091833')
foodCheck.place(relx=0.004, rely=0.71)

        #----------- Drinks Label-----------#
Labeldrinks = tk.Label(root, text="Order Num :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.25)
Labeldrinks = tk.Label(root, text="Jollof Rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.32)
Labeldrinks = tk.Label(root, text="Fried rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.4)
Labeldrinks = tk.Label(root, text="Banku & tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.48)
Labeldrinks = tk.Label(root, text="Fufu & mutton soup :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.56)
Labeldrinks = tk.Label(root, text="Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.64)
Labeldrinks = tk.Label(root, text="Drinks :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks.place(relx=0.28, rely=0.71)

        #----------- Drinks Label-----------#
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.25)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.32)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.4)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.48)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.56)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.64)
entrydrinks = tk.Entry(root, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entrydrinks.place(relx=0.41, rely=0.71)

drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var1, background='#091833')
drinkCheck.place(relx=0.26, rely=0.32)
drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var2, background='#091833')
drinkCheck.place(relx=0.26, rely=0.4)
drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var3, background='#091833')
drinkCheck.place(relx=0.26, rely=0.48)
drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var4, background='#091833')
drinkCheck.place(relx=0.26, rely=0.56)
drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var5, background='#091833')
drinkCheck.place(relx=0.26, rely=0.64)
drinkCheck = Checkbutton(root, onvalue=1, offvalue=0, variable=var6, background='#091833')
drinkCheck.place(relx=0.26, rely=0.71)

#----------- Creating builtin calculator-----------#
i = 0

def get_num(num):
    global i
    display.insert(i, num)
    i += 1

def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def delete_one():
        char = len(display.get())
        display.delete(char-1)

def delete_all():
    display.delete(0, END)

def calculate():
        all_text = display.get()
        try:
                a = parser.expr(all_text).compile()
                result = eval(a)
                delete_all()
                display.insert(0, result)
        except Exception:
                delete_all()
                display.insert(0, "Error")

display = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
display.place(relx=0.780, rely=0.18, height=35, relwidth=0.210)
        
one_button = tk.Button(root, text='''1''', command=lambda :get_num(1), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
one_button.place(relx=0.824, rely=0.24, height=50, width=50)
two_button = tk.Button(root, text='''2''', command=lambda :get_num(2), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
two_button.place(relx=0.865, rely=0.24, height=50, width=50)
three_button = tk.Button(root, text='''3''', command=lambda :get_num(3), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
three_button.place(relx=0.908, rely=0.24, height=50, width=50)        
four_button = tk.Button(root, text='''4''', command=lambda :get_num(4), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
four_button.place(relx=0.824, rely=0.32, height=50, width=50)
five_button = tk.Button(root, text='''5''', command=lambda :get_num(5), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
five_button.place(relx=0.865, rely=0.32, height=50, width=50)
six_button = tk.Button(root, text='''6''', command=lambda :get_num(6), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
six_button.place(relx=0.908, rely=0.32, height=50, width=50)
seven_button = tk.Button(root, text='''7''', command=lambda :get_num(7), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
seven_button.place(relx=0.824, rely=0.40, height=50, width=50)
eight_button = tk.Button(root, text='''8''', command=lambda :get_num(8), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
eight_button.place(relx=0.865, rely=0.40, height=50, width=50)
nine_button = tk.Button(root, text='''9''', command=lambda :get_num(9), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
nine_button.place(relx=0.908, rely=0.40, height=50, width=50)
zero_button = tk.Button(root, text='''0''', command=lambda :get_num(0), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
zero_button.place(relx=0.865, rely=0.48, height=50, width=50)

decimal_button = tk.Button(root, text='''.''', command=lambda :get_operator('.'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
decimal_button.place(relx=0.824, rely=0.48, height=50, width=50)
mod_button = tk.Button(root, text='''%''', command=lambda :get_operator('%'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
mod_button.place(relx=0.908, rely=0.48, height=50, width=50)
del_all_button = tk.Button(root, text='''C''', command=lambda :delete_all(), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
del_all_button.place(relx=0.780, rely=0.24, height=50, width=50)
del_one_button = tk.Button(root, text='''⌫''', command=lambda :delete_one(), bg='red', fg='#ffffff', font=font_5, borderwidth='1')
del_one_button.place(relx=0.780, rely=0.32, height=50, width=50)

add_button = tk.Button(root, text='''+''', command=lambda :get_operator('+'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
add_button.place(relx=0.950, rely=0.24, height=50, width=50)
sub_button = tk.Button(root, text='''-''', command=lambda :get_operator('-'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
sub_button.place(relx=0.950, rely=0.32, height=50, width=50)
mul_button = tk.Button(root, text='''*''', command=lambda :get_operator('*'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
mul_button.place(relx=0.950, rely=0.40, height=50, width=50)
div_button = tk.Button(root, text='''/''', command=lambda :get_operator('/'), bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
div_button.place(relx=0.950, rely=0.48, height=50, width=50)
equal_button = tk.Button(root, text='''=''', command=lambda :calculate(), bg='green', fg='#ffffff', font=font_5, borderwidth='1')
equal_button.place(relx=0.780, rely=0.40, height=105, width=50)

        #----------- List Food Cost-----------#
LabelCost = tk.Label(root, text="Total Food Cost:", font=font_3, fg='red', bg='#091833')
LabelCost.place(relx=0.006, rely=0.87)
Label_service = tk.Label(root, text="Total Drinks Cost:", font=font_3, fg='#bac8bd', bg='#091833')
Label_service.place(relx=0.006, rely=0.91)
Label_tax = tk.Label(root, text="Total ... Cost:", font=font_3, fg='#bac8bd', bg='#091833')
Label_tax.place(relx=0.006, rely=0.95)
Label_subtotal = tk.Label(root, text="Tax:", font=font_3, fg='#bac8bd', bg='#091833')
Label_subtotal.place(relx=0.230, rely=0.87)
Label_subtotal = tk.Label(root, text="Subtotal :", font=font_3, fg='#bac8bd', bg='#091833')
Label_subtotal.place(relx=0.230, rely=0.91)
Label_total = tk.Label(root, text="Total :", font=font_3, fg='#bac8bd', bg='#091833')
Label_total.place(relx=0.230, rely=0.95)


entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=foodcostvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.115, rely=0.87, relwidth=0.050)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=drinkscostvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.115, rely=0.91, relwidth=0.050)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=costvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.115, rely=0.95, relwidth=0.050)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=taxvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.87, relwidth=0.050)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=subtotalvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.91, relwidth=0.050)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=totalvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.95, relwidth=0.050)
        
        #----------- Creating Control Buttons-----------#
control_button = tk.Button(root, text='PRICE', font=font_4, bg='green', fg='#ffffff')
control_button.place(relx=0.917, rely=0.94, height=34, width=55)
control_button = tk.Button(root, text='TOTAL', font=font_4, bg="#f2a343", fg='#ffffff')
control_button.place(relx=0.872, rely=0.94, height=34, width=55)
control_button = tk.Button(root, text='RESET', font=font_4, bg="#f2a343", fg='#ffffff')
control_button.place(relx=0.826, rely=0.94, height=34, width=55)
control_button = tk.Button(root, text='EXIT', font=font_4, bg='red', fg='#ffffff')
control_button.place(relx=0.780, rely=0.94, height=34, width=55)

        #Creating the receipt panel
Receipt = tk.Text(root, font=font_4, width=33, height=16)
Receipt.place(relx=0.780, rely=0.56)

'''Making a main root so that the window will not disappear once the program is run'''
root.mainloop()