from cgitb import text
import tkinter as tk
from tkinter import DISABLED, Checkbutton, Label, Button, IntVar, StringVar
import time

#Displaying login time to the user
localtime = time.asctime(time.localtime(time.time()))

class App1:
    def __init__(self, top):
        self.top = top  #name of the window
        top.title("Restaurant Manager")
        top.geometry("1270x690+0+0")
        top.resizable(False, False)
        top.configure(bg="#091833") #Dark blue colour

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

        self.TitleHeader = tk.Label(master=top, text="RESTAURANT MANAGER", bg="#091833", font=font_2, fg="#f2a343")
        self.TitleHeader.place(relx = 0.268, rely=0.02, height=51, width=507) 

        #Creating label to harbour and display time. Login time doesn't change  
        localtime1 = Label(master=top, text=localtime, bg="#091833", font=font_1, fg="steel blue")
        localtime1.place(relx = 0.420, rely=0.12)  

        #----------- Food Label-----------#
        self.LabelOrder = tk.Label(master=top, text="Order Num :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.25)
        self.LabelOrder = tk.Label(master=top, text="Jollof Rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.32)
        self.LabelOrder = tk.Label(master=top, text="Fried rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.4)
        self.LabelOrder = tk.Label(master=top, text="Banku & tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.48)
        self.LabelOrder = tk.Label(master=top, text="Fufu & mutton soup :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.56)
        self.LabelOrder = tk.Label(master=top, text="Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.64)
        self.LabelOrder = tk.Label(master=top, text="Drinks :", font=font_3, fg='#bac8bd', bg='#091833')
        self.LabelOrder.place(relx=0.025, rely=0.71)

        #----------- Food Label-----------#
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food1, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.25)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food2, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.32)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food3, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.4)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food4, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.48)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food5, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.56)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food6, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.64)
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9',state=DISABLED, textvariable=food7, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.16, rely=0.71)

        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var1, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.32)
        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var2, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.4)
        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var3, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.48)
        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var4, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.56)
        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var5, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.64)
        self.foodCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var6, background='#091833')
        self.foodCheck.place(relx=0.004, rely=0.71)

        #----------- Drinks Label-----------#
        self.Labeldrinks = tk.Label(master=top, text="Order Num :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.25)
        self.Labeldrinks = tk.Label(master=top, text="Jollof Rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.32)
        self.Labeldrinks = tk.Label(master=top, text="Fried rice & chicken :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.4)
        self.Labeldrinks = tk.Label(master=top, text="Banku & tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.48)
        self.Labeldrinks = tk.Label(master=top, text="Fufu & mutton soup :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.56)
        self.Labeldrinks = tk.Label(master=top, text="Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.64)
        self.Labeldrinks = tk.Label(master=top, text="Drinks :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Labeldrinks.place(relx=0.28, rely=0.71)

        #----------- Drinks Label-----------#
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.25)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.32)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.4)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.48)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.56)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.64)
        self.entrydrinks = tk.Entry(master=top, bg='#d9d9d9', width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entrydrinks.place(relx=0.41, rely=0.71)

        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var1, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.32)
        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var2, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.4)
        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var3, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.48)
        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var4, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.56)
        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var5, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.64)
        self.drinkCheck = Checkbutton(master=top, onvalue=1, offvalue=0, variable=var6, background='#091833')
        self.drinkCheck.place(relx=0.26, rely=0.71)

        #----------- Creating builtin calculator-----------#
        self.entryOrder = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryOrder.place(relx=0.780, rely=0.18, height=35, relwidth=0.210)
        
        self.one_button = tk.Button(master=top, text='''1''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.one_button.place(relx=0.824, rely=0.24, height=50, width=50)
        self.two_button = tk.Button(master=top, text='''2''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.two_button.place(relx=0.865, rely=0.24, height=50, width=50)
        self.three_button = tk.Button(master=top, text='''3''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.three_button.place(relx=0.908, rely=0.24, height=50, width=50)
        
        self.four_button = tk.Button(master=top, text='''4''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.four_button.place(relx=0.824, rely=0.32, height=50, width=50)
        self.five_button = tk.Button(master=top, text='''5''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.five_button.place(relx=0.865, rely=0.32, height=50, width=50)
        self.six_button = tk.Button(master=top, text='''6''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.six_button.place(relx=0.908, rely=0.32, height=50, width=50)

        self.seven_button = tk.Button(master=top, text='''7''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.seven_button.place(relx=0.824, rely=0.40, height=50, width=50)
        self.eight_button = tk.Button(master=top, text='''8''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.eight_button.place(relx=0.865, rely=0.40, height=50, width=50)
        self.nine_button = tk.Button(master=top, text='''9''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.nine_button.place(relx=0.908, rely=0.40, height=50, width=50)

        self.zero_button = tk.Button(master=top, text='''0''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.zero_button.place(relx=0.865, rely=0.48, height=50, width=50)
        self.decimal_button = tk.Button(master=top, text='''.''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.decimal_button.place(relx=0.824, rely=0.48, height=50, width=50)
        self.mod_button = tk.Button(master=top, text='''%''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.mod_button.place(relx=0.908, rely=0.48, height=50, width=50)
        self.del_all_button = tk.Button(master=top, text='''C''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.del_all_button.place(relx=0.780, rely=0.24, height=50, width=50)
        self.del_one_button = tk.Button(master=top, text='''⌫''', bg='red', fg='#ffffff', font=font_5, borderwidth='1')
        self.del_one_button.place(relx=0.780, rely=0.32, height=50, width=50)

        self.add_button = tk.Button(master=top, text='''+''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.add_button.place(relx=0.950, rely=0.24, height=50, width=50)
        self.sub_button = tk.Button(master=top, text='''-''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.sub_button.place(relx=0.950, rely=0.32, height=50, width=50)
        self.mul_button = tk.Button(master=top, text='''*''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.mul_button.place(relx=0.950, rely=0.40, height=50, width=50)
        self.div_button = tk.Button(master=top, text='''/''', bg='#122c63', fg='#ffffff', font=font_5, borderwidth='1')
        self.div_button.place(relx=0.950, rely=0.48, height=50, width=50)
        self.equal_button = tk.Button(master=top, text='''=''', bg='green', fg='#ffffff', font=font_5, borderwidth='1')
        self.equal_button.place(relx=0.780, rely=0.40, height=105, width=50)

        #----------- List Food Cost-----------#
        self.LabelCost = tk.Label(master=top, text="Total Food Cost:", font=font_3, fg='red', bg='#091833')
        self.LabelCost.place(relx=0.006, rely=0.87)
        self.Label_service = tk.Label(master=top, text="Total Drinks Cost:", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_service.place(relx=0.006, rely=0.91)
        self.Label_tax = tk.Label(master=top, text="Total ... Cost:", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_tax.place(relx=0.006, rely=0.95)
        self.Label_subtotal = tk.Label(master=top, text="Tax:", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_subtotal.place(relx=0.230, rely=0.87)
        self.Label_subtotal = tk.Label(master=top, text="Subtotal :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_subtotal.place(relx=0.230, rely=0.91)
        self.Label_total = tk.Label(master=top, text="Total :", font=font_3, fg='#bac8bd', bg='#091833')
        self.Label_total.place(relx=0.230, rely=0.95)


        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=foodcostvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.115, rely=0.87, relwidth=0.050)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=drinkscostvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.115, rely=0.91, relwidth=0.050)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=costvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.115, rely=0.95, relwidth=0.050)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=taxvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.291, rely=0.87, relwidth=0.050)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=subtotalvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.291, rely=0.91, relwidth=0.050)
        self.entryCost = tk.Entry(master=top, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=totalvar, selectbackground='#f2a343', selectforeground='#ffffff')
        self.entryCost.place(relx=0.291, rely=0.95, relwidth=0.050)
        
        #----------- Creating Control Buttons-----------#
        self.control_button = tk.Button(master=top, text='PRICE', font=font_4, bg='green', fg='#ffffff')
        self.control_button.place(relx=0.917, rely=0.94, height=34, width=55)
        self.control_button = tk.Button(master=top, text='TOTAL', font=font_4, bg="#f2a343", fg='#ffffff')
        self.control_button.place(relx=0.872, rely=0.94, height=34, width=55)
        self.control_button = tk.Button(master=top, text='RESET', font=font_4, bg="#f2a343", fg='#ffffff')
        self.control_button.place(relx=0.826, rely=0.94, height=34, width=55)
        self.control_button = tk.Button(master=top, text='EXIT', font=font_4, bg='red', fg='#ffffff')
        self.control_button.place(relx=0.780, rely=0.94, height=34, width=55)

        #Creating the receipt panel
        self.Receipt = tk.Text(master=top, font=font_4, width=33, height=16)
        self.Receipt.place(relx=0.780, rely=0.56)

'''Making a main root so that the window will not disappear once the program is run'''
root = tk.Tk()
my_gui = App1(root)
root.mainloop()