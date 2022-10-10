from cgitb import text
import tkinter as tk
from tkinter import DISABLED, END, Checkbutton, Label, Button, IntVar, StringVar
import time
from tkinter.font import NORMAL
import parser

#Displaying login time to the user
localtime = time.asctime(time.localtime(time.time()))

#Functions for checkbutton
def food_1():
        if var1.get()==1:
                food_entry1.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry1.delete(0, END)
                food_entry1.focus()
        else:
                food_entry1.config(state=DISABLED)
                food1.set('0')
def food_2():
        if var2.get()==1:
                food_entry2.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry2.delete(0, END)
                food_entry2.focus()
        else:
                food_entry2.config(state=DISABLED)
                food2.set('0')
def food_3():
        if var3.get()==1:
                food_entry3.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry3.delete(0, END)
                food_entry3.focus()
        else:
                food_entry3.config(state=DISABLED)
                food3.set('0')
def food_4():
        if var4.get()==1:
                food_entry4.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry4.delete(0, END)
                food_entry4.focus()
        else:
                food_entry4.config(state=DISABLED)
                food4.set('0')
def food_5():
        if var5.get()==1:
                food_entry5.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry5.delete(0, END)
                food_entry5.focus()
        else:
                food_entry5.config(state=DISABLED)
                food5.set('0')
def food_6():
        if var6.get()==1:
                food_entry6.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry6.delete(0, END)
                food_entry6.focus()
        else:
                food_entry6.config(state=DISABLED)
                food6.set('0')
def food_7():
        if var7.get()==1:
                food_entry7.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry7.delete(0, END)
                food_entry7.focus()
        else:
                food_entry7.config(state=DISABLED)
                food7.set('0')
def food_8():
        if var8.get()==1:
                food_entry8.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry8.delete(0, END)
                food_entry8.focus()
        else:
                food_entry8.config(state=DISABLED)
                food8.set('0')
def food_9():
        if var9.get()==1:
                food_entry9.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry9.delete(0, END)
                food_entry9.focus()
        else:
                food_entry9.config(state=DISABLED)
                food9.set('0')
def food_10():
        if var10.get()==1:
                food_entry10.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry10.delete(0, END)
                food_entry10.focus()
        else:
                food_entry10.config(state=DISABLED)
                food10.set('0')
def food_11():
        if var11.get()==1:
                food_entry11.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry11.delete(0, END)
                food_entry11.focus()
        else:
                food_entry11.config(state=DISABLED)
                food11.set('0')
def food_12():
        if var12.get()==1:
                food_entry12.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                food_entry12.delete(0, END)
                food_entry12.focus()
        else:
                food_entry12.config(state=DISABLED)
                food12.set('0')

def drinks_1():
        if var13.get()==1:
                entryDrinks1.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks1.delete(0, END)
                entryDrinks1.focus()
        else:
                entryDrinks1.config(state=DISABLED)
                drinks1.set('0')
def drinks_2():
        if var14.get()==1:
                entryDrinks2.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks2.delete(0, END)
                entryDrinks2.focus()
        else:
                entryDrinks2.config(state=DISABLED)
                drinks2.set('0')
def drinks_3():
        if var15.get()==1:
                entryDrinks3.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks3.delete(0, END)
                entryDrinks3.focus()
        else:
                entryDrinks3.config(state=DISABLED)
                drinks3.set('0')
def drinks_4():
        if var16.get()==1:
                entryDrinks4.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks4.delete(0, END)
                entryDrinks4.focus()
        else:
                entryDrinks4.config(state=DISABLED)
                drinks4.set('0')
def drinks_5():
        if var17.get()==1:
                entryDrinks5.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks5.delete(0, END)
                entryDrinks5.focus()
        else:
                entryDrinks5.config(state=DISABLED)
                drinks5.set('0')
def drinks_6():
        if var18.get()==1:
                entryDrinks6.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks6.delete(0, END)
                entryDrinks6.focus()
        else:
                entryDrinks6.config(state=DISABLED)
                drinks6.set('0')
def drinks_7():
        if var19.get()==1:
                entryDrinks7.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks7.delete(0, END)
                entryDrinks7.focus()
        else:
                entryDrinks7.config(state=DISABLED)
                drinks7.set('0')
def drinks_8():
        if var20.get()==1:
                entryDrinks8.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks8.delete(0, END)
                entryDrinks8.focus()
        else:
                entryDrinks8.config(state=DISABLED)
                drinks8.set('0')
def drinks_9():
        if var21.get()==1:
                entryDrinks9.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks9.delete(0, END)
                entryDrinks9.focus()
        else:
                entryDrinks9.config(state=DISABLED)
                drinks9.set('0')
def drinks_10():
        if var22.get()==1:
                entryDrinks10.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks10.delete(0, END)
                entryDrinks10.focus()
        else:
                entryDrinks10.config(state=DISABLED)
                drinks10.set('0')
def drinks_11():
        if var23.get()==1:
                entryDrinks11.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks11.delete(0, END)
                entryDrinks11.focus()
        else:
                entryDrinks11.config(state=DISABLED)
                drinks11.set('0')
def drinks_12():
        if var24.get()==1:
                entryDrinks12.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDrinks12.delete(0, END)
                entryDrinks12.focus()
        else:
                entryDrinks12.config(state=DISABLED)
                drinks12.set('0')

def deli_1():
        if var25.get()==1:
                entryDeli1.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli1.delete(0, END)
                entryDeli1.focus()
        else:
                entryDeli1.config(state=DISABLED)
                deli1.set('0')
def deli_2():
        if var26.get()==1:
                entryDeli2.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli2.delete(0, END)
                entryDeli2.focus()
        else:
                entryDeli2.config(state=DISABLED)
                deli2.set('0')
def deli_3():
        if var27.get()==1:
                entryDeli3.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli3.delete(0, END)
                entryDeli3.focus()
        else:
                entryDeli3.config(state=DISABLED)
                deli3.set('0')
def deli_4():
        if var28.get()==1:
                entryDeli4.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli4.delete(0, END)
                entryDeli4.focus()
        else:
                entryDeli4.config(state=DISABLED)
                deli4.set('0')
def deli_5():
        if var29.get()==1:
                entryDeli5.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli5.delete(0, END)
                entryDeli5.focus()
        else:
                entryDeli5.config(state=DISABLED)
                deli5.set('0')
def deli_6():
        if var30.get()==1:
                entryDeli6.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli6.delete(0, END)
                entryDeli6.focus()
        else:
                entryDeli6.config(state=DISABLED)
                deli6.set('0')
def deli_7():
        if var31.get()==1:
                entryDeli7.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli7.delete(0, END)
                entryDeli7.focus()
        else:
                entryDeli7.config(state=DISABLED)
                deli7.set('0')
def deli_8():
        if var32.get()==1:
                entryDeli8.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli8.delete(0, END)
                entryDeli8.focus()
        else:
                entryDeli8.config(state=DISABLED)
                deli8.set('0')
def deli_9():
        if var33.get()==1:
                entryDeli9.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli9.delete(0, END)
                entryDeli9.focus()
        else:
                entryDeli9.config(state=DISABLED)
                deli9.set('0')
def deli_10():
        if var34.get()==1:
                entryDeli10.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli10.delete(0, END)
                entryDeli10.focus()
        else:
                entryDeli1.config(state=DISABLED)
                deli10.set('0')
def deli_11():
        if var35.get()==1:
                entryDeli11.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli11.delete(0, END)
                entryDeli11.focus()
        else:
                entryDeli11.config(state=DISABLED)
                deli11.set('0')
def deli_12():
        if var36.get()==1:
                entryDeli12.config(state=NORMAL)  #Changing state of the checkbutton in the entry display
                entryDeli12.delete(0, END)
                entryDeli12.focus()
        else:
                entryDeli12.config(state=DISABLED)
                deli12.set('0')

'''============Start============Functions for the control buttons============Start============'''
def total_cost():
        #Getting the quantities from the empty fields
        item1 = int(food1.get())   #Converting the string from empty fields into int
        item2 = int(food2.get())
        item3 = int(food3.get())
        item4 = int(food4.get())
        item5 = int(food5.get())
        item6 = int(food6.get())
        item7 = int(food7.get())
        item8 = int(food8.get())
        item9 = int(food9.get())
        item10 = int(food10.get())
        item11 = int(food11.get())
        item12 = int(food12.get())

        item13 = int(drinks1.get())   #Converting the string from empty fields into int
        item14 = int(drinks2.get())
        item15 = int(drinks3.get())
        item16 = int(drinks4.get())
        item17 = int(drinks5.get())
        item18 = int(drinks6.get())
        item19 = int(drinks7.get())
        item20 = int(drinks8.get())
        item21 = int(drinks9.get())
        item22 = int(drinks10.get())
        item23 = int(drinks11.get())
        item24 = int(drinks12.get())

        item25 = int(deli1.get())   #Converting the string from empty fields into int
        item26 = int(deli2.get())
        item27 = int(deli3.get())
        item28 = int(deli4.get())
        item29 = int(deli5.get())
        item30 = int(deli6.get())
        item31 = int(deli7.get())
        item32 = int(deli8.get())
        item33 = int(deli9.get())
        item34 = int(deli10.get())
        item35 = int(deli11.get())
        item36 = int(deli12.get())

#Calculating the prices of items       
        food_price1 = 100
        food_price2 = 15
        food_price3 = 32
        food_price4 = 41
        food_price5 = 25
        food_price6 = 50
        food_price7 = 75
        food_price8 = 48
        food_price9 = 55
        food_price10 = 62
        food_price11 = 38
        food_price12 = 83

        foodPrices = (item1*food_price1) + (item2*food_price2) + (item3*food_price3) + (item4*food_price4) \
                + (item5*food_price5) + (item6*food_price6) + (item7*food_price7) + (item8*food_price8) + (item9*food_price9) \
                        + (item10*food_price10) +  (item11*food_price11) + (item12*food_price12)

        drink_price1 = 5
        drink_price2 = 5
        drink_price3 = 10
        drink_price4 = 30
        drink_price5 = 11
        drink_price6 = 25
        drink_price7 = 31
        drink_price8 = 35
        drink_price9 = 50
        drink_price10 = 43
        drink_price11 = 40
        drink_price12 = 20

        drinkPrices = (item13*drink_price1) + (item14*drink_price2) + (item15*drink_price3) + (item16*drink_price4) \
                + (item17*drink_price5) + (item18*drink_price6) + (item19*drink_price7) + (item20*drink_price8) + (item21*drink_price9) \
                        + (item22*drink_price10) +  (item23*drink_price11) + (item24*drink_price12)

        deli_price1 = 5
        deli_price2 = 5
        deli_price3 = 10
        deli_price4 = 30
        deli_price5 = 11
        deli_price6 = 25
        deli_price7 = 31
        deli_price8 = 35
        deli_price9 = 50
        deli_price10 = 43
        deli_price11 = 40
        deli_price12 = 20

        deliPrices = (item25*deli_price1) + (item26*deli_price2) + (item27*deli_price3) + (item28*deli_price4) \
                + (item29*deli_price5) + (item30*deli_price6) + (item31*deli_price7) + (item32*deli_price8) + (item33*deli_price9) \
                        + (item34*deli_price10) +  (item35*deli_price11) + (item36*deli_price12)

        #Calculating subtotal        
        sub_total_price = foodPrices + drinkPrices + deliPrices
        #Calculating tax
        serviceTax = sub_total_price * 0.17
        costs_sum = sub_total_price + serviceTax
        #Adding costs to the entry
        foodcostvar.set('₵' + str(foodPrices))
        drinkscostvar.set('₵' + str(drinkPrices))
        delicostvar.set('₵' + str(deliPrices))
        taxvar.set('₵' + str(serviceTax))
       # subtotalvar = StringVar()
        subtotalvar.set('₵' + str(sub_total_price))
     #   totalvar = StringVar()
        totalvar.set('₵' + str(costs_sum))

    #    serviceTax.set('17.5')
'''============End============Functions for the control buttons============Start============'''

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
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()

food1 = StringVar()
food2 = StringVar()
food3 = StringVar()
food4 = StringVar()
food5 = StringVar()
food6 = StringVar()
food7 = StringVar()
food8 = StringVar()
food9 = StringVar()
food10 = StringVar()
food11 = StringVar()
food12 = StringVar()

drinks1 = StringVar()
drinks2 = StringVar()
drinks3 = StringVar()
drinks4 = StringVar()
drinks5 = StringVar()
drinks6 = StringVar()
drinks7 = StringVar()
drinks8 = StringVar()
drinks9 = StringVar()
drinks10 = StringVar()
drinks11 = StringVar()
drinks12 = StringVar()

deli1 = StringVar()
deli2 = StringVar()
deli3 = StringVar()
deli4 = StringVar()
deli5 = StringVar()
deli6 = StringVar()
deli7 = StringVar()
deli8 = StringVar()
deli9 = StringVar()
deli10 = StringVar()
deli11 = StringVar()
deli12 = StringVar()

#Setting empty fields to zero
food1.set('0')
food2.set('0')
food3.set('0')
food4.set('0')
food5.set('0')
food6.set('0')
food7.set('0')
food8.set('0')
food9.set('0')
food10.set('0')
food11.set('0')
food12.set('0')

drinks1.set('0')
drinks2.set('0')
drinks3.set('0')
drinks4.set('0')
drinks5.set('0')
drinks6.set('0')
drinks7.set('0')
drinks8.set('0')
drinks9.set('0')
drinks10.set('0')
drinks11.set('0')
drinks12.set('0')

deli1.set('0')
deli2.set('0')
deli3.set('0')
deli4.set('0')
deli5.set('0')
deli6.set('0')
deli7.set('0')
deli8.set('0')
deli9.set('0')
deli10.set('0')
deli11.set('0')
deli12.set('0')

#Costs entry
foodcostvar = StringVar()
drinkscostvar = StringVar()
delicostvar = StringVar()
taxvar = StringVar()
subtotalvar = StringVar()
totalvar = StringVar()

#----------- Food Info-----------#

TitleHeader = tk.Label(root, text="RESTAURANT MANAGER", bg="#091833", font=font_2, fg="#f2a343")
TitleHeader.place(relx = 0.268, rely=0.02, height=51, width=507) 

#Creating label to harbour and display time. Login time doesn't change  
localtime1 = Label(root, text=localtime, bg="#091833", font=font_1, fg="steel blue")
localtime1.place(relx = 0.420, rely=0.12)  

'''============Start============Designing the Food UI============Start============'''
#----------- Food Label-----------#
LabelOrder = tk.Label(root, text="Full Grilled Chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.18)
LabelOrder = tk.Label(root, text="Jollof Rice & Chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.23)
LabelOrder = tk.Label(root, text="Fried Rice & Chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.28)
LabelOrder = tk.Label(root, text="Banku & Grilled Tilapia :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.33)
LabelOrder = tk.Label(root, text="Fufu & Mutton Soup :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.38)
LabelOrder = tk.Label(root, text="Red Red :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.43)
LabelOrder = tk.Label(root, text="Yam & Palava Sauce :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.48)
LabelOrder = tk.Label(root, text="Rice Balls & Groundnut Soup :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.53)
LabelOrder = tk.Label(root, text="Grilled Pork & Banku :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.58)
LabelOrder = tk.Label(root, text="Pepper Soup :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.63)
LabelOrder = tk.Label(root, text="TZ & Ayoyo Soup :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.68)
LabelOrder = tk.Label(root, text="Waakye :", font=font_3, fg='#bac8bd', bg='#091833')
LabelOrder.place(relx=0.025, rely=0.73)

        #----------- Food Entry-----------#
food_entry1 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food1, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry1.place(relx=0.16, rely=0.18)
food_entry2 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food2, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry2.place(relx=0.16, rely=0.23)
food_entry3 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food3, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry3.place(relx=0.16, rely=0.28)
food_entry4 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food4, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry4.place(relx=0.16, rely=0.33)
food_entry5 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food5, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry5.place(relx=0.16, rely=0.38)
food_entry6 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food6, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry6.place(relx=0.16, rely=0.43)
food_entry7 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food7, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry7.place(relx=0.16, rely=0.48)
food_entry8 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food8, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry8.place(relx=0.16, rely=0.53)
food_entry9 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food9, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry9.place(relx=0.16, rely=0.58)
food_entry10 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food10, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry10.place(relx=0.16, rely=0.63)
food_entry11 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food11, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry11.place(relx=0.16, rely=0.68)
food_entry12 = tk.Entry(root, bg='#d9d9d9', state=DISABLED, textvariable=food12, width=7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
food_entry12.place(relx=0.16, rely=0.73)

foodCheck_0ne = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_1, variable=var1, background='#091833')
foodCheck_0ne.place(relx=0.004, rely=0.18)
foodCheck_two = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_2, variable=var2, background='#091833')
foodCheck_two.place(relx=0.004, rely=0.23)
foodCheck_three = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_3, variable=var3, background='#091833')
foodCheck_three.place(relx=0.004, rely=0.28)
foodCheck_four = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_4, variable=var4, background='#091833')
foodCheck_four.place(relx=0.004, rely=0.33)
foodCheck_five = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_5, variable=var5, background='#091833')
foodCheck_five.place(relx=0.004, rely=0.38)
foodCheck_six = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_6, variable=var6, background='#091833')
foodCheck_six.place(relx=0.004, rely=0.43)
foodCheck_seven = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_7, variable=var7, background='#091833')
foodCheck_seven.place(relx=0.004, rely=0.48)
foodCheck_eight = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_8, variable=var8, background='#091833')
foodCheck_eight.place(relx=0.004, rely=0.53)
foodCheck_nine = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_9, variable=var9, background='#091833')
foodCheck_nine.place(relx=0.004, rely=0.58)
foodCheck_ten = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_10, variable=var10, background='#091833')
foodCheck_ten.place(relx=0.004, rely=0.63)
foodCheck_eleven = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_11, variable=var11, background='#091833')
foodCheck_eleven.place(relx=0.004, rely=0.68)
foodCheck_twelve = tk.Checkbutton(root, onvalue=1, offvalue=0, command=food_12, variable=var12, background='#091833')
foodCheck_twelve.place(relx=0.004, rely=0.73)

'''============End============Designing the Food UI============End============'''

'''============Start============Designing the Drinks UI============Start============'''
        #----------- Drinks Label-----------#
Labeldrinks1 = tk.Label(root, text="Fanta :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks1.place(relx=0.28, rely=0.18)
Labeldrinks2 = tk.Label(root, text="Coca Cola :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks2.place(relx=0.28, rely=0.23)
Labeldrinks3 = tk.Label(root, text="Malta Guinness(bottle) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks3.place(relx=0.28, rely=0.28)
Labeldrinks4 = tk.Label(root, text="Don Simon :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks4.place(relx=0.28, rely=0.33)
Labeldrinks5 = tk.Label(root, text="Malta Guinness(Can) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks5.place(relx=0.28, rely=0.38)
Labeldrinks5 = tk.Label(root, text="Root Beer(Can) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks5.place(relx=0.28, rely=0.43)
Labeldrinks5 = tk.Label(root, text="Star Beer(Can) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks5.place(relx=0.28, rely=0.48)
Labeldrinks6 = tk.Label(root, text="Club Beer(bottle) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks6.place(relx=0.28, rely=0.53)
Labeldrinks7 = tk.Label(root, text="Vodka :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks7.place(relx=0.28, rely=0.58)
Labeldrinks8 = tk.Label(root, text="Club Beer(can) :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks8.place(relx=0.28, rely=0.63)
Labeldrinks9 = tk.Label(root, text="Jonnie Walker :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks9.place(relx=0.28, rely=0.68)
Labeldrinks10 = tk.Label(root, text="Heineken :", font=font_3, fg='#bac8bd', bg='#091833')
Labeldrinks10.place(relx=0.28, rely=0.73)

        #----------- Drinks Label-----------#
entryDrinks1 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks1, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks1.place(relx=0.43, rely=0.18)
entryDrinks2 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks2, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks2.place(relx=0.43, rely=0.23)
entryDrinks3 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks3, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks3.place(relx=0.43, rely=0.28)
entryDrinks4 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks4, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks4.place(relx=0.43, rely=0.33)
entryDrinks5 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks5, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks5.place(relx=0.43, rely=0.38)
entryDrinks6 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks6, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks6.place(relx=0.43, rely=0.43)
entryDrinks7 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks7.place(relx=0.43, rely=0.48)
entryDrinks8 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks8, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks8.place(relx=0.43, rely=0.53)
entryDrinks9 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks9, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks9.place(relx=0.43, rely=0.58)
entryDrinks10 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks10, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks10.place(relx=0.43, rely=0.63)
entryDrinks11 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks11, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks11.place(relx=0.43, rely=0.68)
entryDrinks12 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=drinks12, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDrinks12.place(relx=0.43, rely=0.73)

drink1 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_1, variable=var13, background='#091833')
drink1.place(relx=0.26, rely=0.18)
drink2 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_2, variable=var14, background='#091833')
drink2.place(relx=0.26, rely=0.23)
drink3 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_3, variable=var15, background='#091833')
drink3.place(relx=0.26, rely=0.28)
drink4 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_4, variable=var16, background='#091833')
drink4.place(relx=0.26, rely=0.33)
drink5 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_5, variable=var17, background='#091833')
drink5.place(relx=0.26, rely=0.38)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_6, variable=var18, background='#091833')
drink6.place(relx=0.26, rely=0.43)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_7, variable=var19, background='#091833')
drink6.place(relx=0.26, rely=0.48)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_8, variable=var20, background='#091833')
drink6.place(relx=0.26, rely=0.53)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_9, variable=var21, background='#091833')
drink6.place(relx=0.26, rely=0.58)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_10, variable=var22, background='#091833')
drink6.place(relx=0.26, rely=0.63)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_11, variable=var23, background='#091833')
drink6.place(relx=0.26, rely=0.68)
drink6 = Checkbutton(root, onvalue=1, offvalue=0, command=drinks_12, variable=var24, background='#091833')
drink6.place(relx=0.26, rely=0.73)

'''============End============Designing the Drinks UI============End============'''

'''============Start============Designing the Delicacies UI============Start============'''
        #----------- Drinks Label-----------#
LabelDeli1 = tk.Label(root, text="Chicken Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli1.place(relx=0.54, rely=0.18)
LabelDeli2 = tk.Label(root, text="Beef Pizza :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli2.place(relx=0.54, rely=0.23)
LabelDeli3 = tk.Label(root, text="Mango Smoothie :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli3.place(relx=0.54, rely=0.28)
LabelDeli4 = tk.Label(root, text="Banana Smoothie :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli4.place(relx=0.54, rely=0.33)
LabelDeli5 = tk.Label(root, text="Mixed Smoothie :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli5.place(relx=0.54, rely=0.38)
LabelDeli6 = tk.Label(root, text="Shawarma :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli6.place(relx=0.54, rely=0.43)
LabelDeli7 = tk.Label(root, text="Sausage :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli7.place(relx=0.54, rely=0.48)
LabelDeli8 = tk.Label(root, text="Salad :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli8.place(relx=0.54, rely=0.53)
LabelDeli9 = tk.Label(root, text="Cookies :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli9.place(relx=0.54, rely=0.58)
LabelDeli10 = tk.Label(root, text="Potato Fries & Chicken :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli10.place(relx=0.54, rely=0.63)
LabelDeli11 = tk.Label(root, text="Cup Cake :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli11.place(relx=0.54, rely=0.68)
LabelDeli12 = tk.Label(root, text="Sandwich :", font=font_3, fg='#bac8bd', bg='#091833')
LabelDeli12.place(relx=0.54, rely=0.73)

        #----------- Drinks Label-----------#
entryDeli1 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli1, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli1.place(relx=0.69, rely=0.18)
entryDeli2 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli2, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli2.place(relx=0.69, rely=0.23)
entryDeli3 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli3, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli3.place(relx=0.69, rely=0.28)
entryDeli4 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli4, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli4.place(relx=0.69, rely=0.33)
entryDeli5 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli5, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli5.place(relx=0.69, rely=0.38)
entryDeli6 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli6, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli6.place(relx=0.69, rely=0.43)
entryDeli7 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli7, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli7.place(relx=0.69, rely=0.48)
entryDeli8 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli8, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli8.place(relx=0.69, rely=0.53)
entryDeli9 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli9, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli9.place(relx=0.69, rely=0.58)
entryDeli10 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli10, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli10.place(relx=0.69, rely=0.63)
entryDeli11 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli11, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli11.place(relx=0.69, rely=0.68)
entryDeli12 = tk.Entry(root, bg='#d9d9d9', width=7, textvariable=deli12, fg='#c60000', font=font_3, selectbackground='#f2a343', selectforeground='#ffffff')
entryDeli12.place(relx=0.69, rely=0.73)

deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_1, variable=var25, background='#091833')
deliCheck.place(relx=0.52, rely=0.18)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_2, variable=var26, background='#091833')
deliCheck.place(relx=0.52, rely=0.23)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_3, variable=var27, background='#091833')
deliCheck.place(relx=0.52, rely=0.28)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_4, variable=var28, background='#091833')
deliCheck.place(relx=0.52, rely=0.33)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_5, variable=var29, background='#091833')
deliCheck.place(relx=0.52, rely=0.38)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_6, variable=var30, background='#091833')
deliCheck.place(relx=0.52, rely=0.43)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_7, variable=var31, background='#091833')
deliCheck.place(relx=0.52, rely=0.48)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_8, variable=var32, background='#091833')
deliCheck.place(relx=0.52, rely=0.53)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_9, variable=var33, background='#091833')
deliCheck.place(relx=0.52, rely=0.58)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_10, variable=var34, background='#091833')
deliCheck.place(relx=0.52, rely=0.63)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_11, variable=var35, background='#091833')
deliCheck.place(relx=0.52, rely=0.68)
deliCheck = Checkbutton(root, onvalue=1, offvalue=0, command=deli_12, variable=var36, background='#091833')
deliCheck.place(relx=0.52, rely=0.73)

'''============End============Designing the Delicacies UI============End============'''

'''============Start============Designing the Costs UI============Start============'''
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
entryCost.place(relx=0.115, rely=0.87, relwidth=0.065)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=drinkscostvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.115, rely=0.91, relwidth=0.065)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=delicostvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.115, rely=0.95, relwidth=0.065)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=taxvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.87, relwidth=0.085)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=subtotalvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.91, relwidth=0.085)
entryCost = tk.Entry(root, bg='#d9d9d9', fg='#c60000', font=font_1, state='readonly', textvariable=totalvar, selectbackground='#f2a343', selectforeground='#ffffff')
entryCost.place(relx=0.291, rely=0.95, relwidth=0.085)

'''============End============Designing the Costs UI============End============'''

'''============Start============Designing the Costs Controls============Start============'''
        #----------- Creating Control Buttons-----------#
control_button = tk.Button(root, text='TOTAL', command=total_cost, font=font_4, bg='red', fg='#ffffff')
control_button.place(relx=0.780, rely=0.94, height=34, width=55)  
control_button = tk.Button(root, text='RESET', font=font_4, bg="#f2a343", fg='#ffffff')
control_button.place(relx=0.826, rely=0.94, height=34, width=55) 
control_button = tk.Button(root, text='SAVE', font=font_4, bg="#f2a343", fg='#ffffff')
control_button.place(relx=0.872, rely=0.94, height=34, width=55)     
control_button = tk.Button(root, text='PRICE', font=font_4, bg='green', fg='#ffffff')
control_button.place(relx=0.917, rely=0.94, height=34, width=55)

'''============End============Designing the Costs UI============End============'''

        #Creating the receipt panel
Receipt = tk.Text(root, font=font_4, width=33, height=16)
Receipt.place(relx=0.780, rely=0.56)

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

'''Making a main root so that the window will not disappear once the program is run'''
root.mainloop()