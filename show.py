from turtle import *
from tkinter import *
import pick as p
import tkinter.messagebox as mb
import os as o
#create a class for the game
class XO: 
    ht()
    def __init__(self,count=0): #create a constructor for the class
        self.c= Screen()._root
        self.count=count
        self.c.resizable(False, False)

        #creare buttons for the game
        self.button1=Button(self.c, text='1', font=('Arial',20),command=lambda: self.click(self.button1),width=5,height=2)
        self.button2=Button(self.c, text='2', font=('Arial',20),command=lambda: self.click(self.button2),width=5,height=2)
        self.button3=Button(self.c, text='3', font=('Arial',20),command=lambda: self.click(self.button3),width=5,height=2)
        self.button4=Button(self.c, text='4', font=('Arial',20),command=lambda: self.click(self.button4),width=5,height=2)
        self.button5=Button(self.c, text='5', font=('Arial',20),command=lambda: self.click(self.button5),width=5,height=2)
        self.button6=Button(self.c, text='6', font=('Arial',20),command=lambda: self.click(self.button6),width=5,height=2)
        self.button7=Button(self.c, text='7', font=('Arial',20),command=lambda: self.click(self.button7),width=5,height=2)
        self.button8=Button(self.c, text='8', font=('Arial',20),command=lambda: self.click(self.button8),width=5,height=2)
        self.button9=Button(self.c, text='9', font=('Arial',20),command=lambda: self.click(self.button9),width=5,height=2)

        #create player1 inputs
        self.label1=Label(self.c, text='Player1 : ', font=('Arial',20),bg='white')
        self.label1.place(x=330,y=500)

        self.button_player1=Button(self.c, text='Enter X',font=('Arial',15),command=lambda: self.click_player(self.button_player1,self.player1))
        self.button_player1.place(x=700,y=500)

        self.player1=Entry(self.c, font=('Arial',20),width=15,bd=2)
        self.player1.place(x=445,y=500)

        #create player2 inputs
        self.label2=Label(self.c, text='Player2 : ', font=('Arial',20),bg='white')
        self.label2.place(x=330,y=580)

        self.button_player2=Button(self.c, text='Enter O',font=('Arial',15),command=lambda: self.click_player(self.button_player2,self.player2))
        self.button_player2.place(x=700,y=580)

        self.player2=Entry(self.c, font=('Arial',20),width=15,bd=2)
        self.player2.place(x=445,y=580)
        
        
    def click_player(self,button_player,entry_player):

        #handling the spaace or nothing input
        if entry_player.get()=='':
            mb.showerror('Invalid Name','Please Enter player name')
            return
        
        for i in entry_player.get():
            self.case=True
            if i ==' ':
                self.case=True
            else:
                self.case=False
                break

        if self.case==True:
            mb.showerror('Invalid Name','Please Enter player name')
            return
        
        #save the player name
        if entry_player == self.player1:
            self.p1=entry_player.get()
        else:
            self.p2=entry_player.get()
        
        #save the place of the player name

        self.n=entry_player.get()   
        self.name=Label(self.c,text=self.n,font=('Arial',20),bg='white')
        self.name.place(x=entry_player.winfo_x(),y=entry_player.winfo_y())

        #destroy the entry and button

        entry_player.destroy()
        button_player.destroy()

        # counter to check if the player name is entered
        self.count+=1
        if self.count==2:
            self.board()
            self.button_place()
            p.OX(game.p1,game.p2)

    def click(self,button_num): #replace the button with the player symbol

        p.turn(button_num['text'])
        button_num.destroy()

    def board(self): #draw the board of the game
        speed(0)
        setheading(90)
        forward(400)
        backward(250)
        setheading(0)
        backward(200)
        forward(550)
        backward(200)
        setheading(270)
        forward(150)
        backward(400)
        forward(150)
        setheading(0)
        forward(200)
        backward(550)

    def button_place(self): #place the buttons on the board

        self.button1.place(x=335,y=50)
        self.button2.place(x=515,y=50)
        self.button3.place(x=700,y=50)
        self.button4.place(x=335,y=164)
        self.button5.place(x=515,y=164)
        self.button6.place(x=700,y=164)
        self.button7.place(x=335,y=280)
        self.button8.place(x=515,y=280)
        self.button9.place(x=700,y=280)

game=XO() #create an instance of the class

done() #run the game