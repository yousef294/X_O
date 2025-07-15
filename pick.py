from turtle import *
R=True
count=0
W_L=   [[1,2,3],
        [4,5,6],
        [7,8,9]]

def enter_num(num):
    global O_X,W_L
    if num =='1':
        one()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[0][0] = O_X
        
    elif num =='2':
        two()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[0][1] = O_X
        
    elif num =='3':
        three()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[0][2] = O_X
        
    elif num =='4':
        four()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[1][0] = O_X
        
    elif num =='5':   
        five()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[1][1] = O_X
        
    elif num =='6':
        six()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[1][2] = O_X
        
    elif num =='7':
        seven()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[2][0] = O_X
        
    elif num =='8':   
        eight()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[2][1] = O_X
        
    elif num =='9':
        nine()
        write(O_X, font=('Arial', 30, 'normal'))
        W_L[2][2] = O_X
        
def OX(p1,p2):
    global player1,player2,O_X,d,X,O,count

    player1 = p1
    player2 = p2
    O_X = 'X'
    X=player1
    O=player2

def turn(number):
    global O_X, player1, player2, R, count

    if R:
        enter_num(number)
    count+=1
    win_check()
    check()

def win_check():
    global W_L,R,O,X
    
    for i in range(len(W_L)):
        if W_L[i][0] == W_L[i][1] == W_L[i][2]:
            penup()
            goto(-50,-300)
            if W_L[i][0] == 'X':
                write(f'{X} is the Winner', font=('Arial', 30, 'normal'))
            else:
                write(f'{O} is the Winner', font=('Arial', 30, 'normal'))
            R=False

        if W_L[0][i] == W_L[1][i] == W_L[2][i]:
            penup()
            goto(-50,-300)
            if W_L[0][i] == 'X':
                write(f'{X} is the Winner', font=('Arial', 30, 'normal'))
            else:
                write(f'{O} is the Winner', font=('Arial', 30, 'normal'))
            R=False

    if W_L[0][0] == W_L[1][1] == W_L[2][2]:
        penup()
        goto(-50,-300)
        if W_L[0][0] == 'X':
            write(f'{X} is the Winner', font=('Arial', 30, 'normal'))
        else:
            write(f'{O} is the Winner', font=('Arial', 30, 'normal'))
        R=False

    if W_L[0][2] == W_L[1][1] == W_L[2][0]:
        penup()
        goto(-50,-300)
        if W_L[0][0] == 'X':
            write(f'{X} is the Winner', font=('Arial', 30, 'normal'))
        else:
            write(f'{O} is the Winner', font=('Arial', 30, 'normal'))
        R=False
        
    if count==9 and R==True:
        penup()
        goto(-50,-300)
        write('Draw', font=('Arial', 30, 'normal'))
        R=False

def check():
        global O_X
        if O_X == 'X':
            O_X = 'O'
        else:
            O_X = 'X'
def one():
    penup()
    goto(-100, 300)
    pendown()

   
def two(): 
    penup()
    goto(65, 300) 
    pendown()


def three():
    penup()
    goto(230, 300)
    pendown()


def four():
    penup()
    goto(-100, 180)
    pendown()


def five():
    penup()
    goto(65, 180)
    pendown()


def six():
    penup()
    goto(230, 180)
    pendown()


def seven():
    penup()
    goto(-100, 60)
    pendown()


def eight():
    penup()
    goto(65, 60)
    pendown()


def nine():
    penup()
    goto(230, 60)
    pendown()