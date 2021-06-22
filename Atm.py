from tkinter import *

top = Tk()  
balance=0
Ddata=""
State=1
  
class Atm(object):

   
    top.geometry("200x100")  
  
    def withdraw(): 
        global balance

        data=int(input("enter the amount to withdraw :"))
        print("amount dedected")
        balance = balance-data
        print("Your current balance :"+str(balance))

    def Deposit():  
        global balance
        global Ddata 
        global State 

        data=int(input("enter the amount to Deposite :"))
        Ddata=data
        State += 1
        print("amount added")
        balance=balance+data
        print("Your current balance :"+str(balance))

  
    b1 = Button(top,text = "Withdraw",command = withdraw,activeforeground = "red",activebackground = "pink",pady=10)  
    b2 = Button(top,text = "Deposite",command = Deposit,activeforeground = "red",activebackground = "pink",pady=10)  

    b1.pack(side = LEFT) 
    b2.pack(side = RIGHT) 




  

  
    top.mainloop()  