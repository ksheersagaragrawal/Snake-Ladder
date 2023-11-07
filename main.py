# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import turtle
import random
scr=turtle.Screen()
scr.title('snake & ladder')
scr.bgpic('Snake.gif')
yellow=turtle.Turtle()
yellow.shape("circle")
yellow.hideturtle()
yellow.penup()
yellow.goto(-265, -155) 
yellow.color(1.0,1.0,0.0)      
yellow.showturtle()     
yellow.speed(1)
blue=turtle.Turtle()
blue.shape("circle")
blue.color(0.0,0.0,1.0)
blue.hideturtle()
blue.penup()
blue.goto(-265,-185)
blue.showturtle() 
blue.speed(1)
d={}
bluepos=1
yellowpos=1
d[1]=[-275,-170]
d[2]=[-170,-170]
d[3]=[-65,-170]
d[4]=[40,-170]
d[5]=[145,-170]
d[6]=[250,-170]
d[7]=[250,-90]
d[8]=[145,-90]
d[9]=[40,-90]
d[10]=[-65,-90]
d[11]=[-170,-90]
d[12]=[-275,-90]
d[13]=[-275,-10]
d[14]=[-170,-10]
d[15]=[-65,-10]
d[16]=[40,-10]
d[17]=[145,-10]
d[18]=[250,-10]
d[19]=[250,70]
d[20]=[145,70]
d[21]=[40,70]
d[22]=[-65,70]
d[23]=[-170,70]
d[24]=[-275,70]
d[25]=[-275,150]
d[26]=[-170,150]
d[27]=[-65,150]
d[28]=[40,150]
d[29]=[145,150]
d[30]=[250,150]
def ladder(pos):
    if pos==3:
        newpos=22
    elif pos==5:
        newpos=8
    elif pos==11:
        newpos=26
    elif pos==20:
        newpos=29
    else:
        newpos=0
    return newpos    
def snake(pos): 
    if pos==27:
        newpos=1
    elif pos==19:
        newpos=7
    elif pos==17:
        newpos=4
    elif pos==21:
        newpos=9
    else:
        newpos=0
    return newpos
flag=1
def dicerollyellow():
    global yellowroll,yellowpos,flag   
    while yellowpos<30 and bluepos<30 and flag==1:
            yellowroll=random.randint(1,6)
            yellowgo=[]
            for j in range(yellowpos+1,yellowpos+yellowroll+1):
                yellowgo.append(j)
            for i in yellowgo:
                if i<=30:
                    yellow.goto(d[i][0],d[i][1])
                    yellowpos=yellowpos+1
                else:
                    break 
            if ladder(yellowpos)!=0:
                yellow.goto(d[ladder(yellowpos)][0],d[ladder(yellowpos)][1])
                yellowpos=ladder(yellowpos)
            if snake(yellowpos)!=0:
                yellow.goto(d[snake(yellowpos)][0],d[snake(yellowpos)][1])
                yellowpos=snake(yellowpos)  
            if yellowpos>=30:
                yellow.write("Winner!", font=("Verdana",  15, "normal")) 
                blue.write("Loser!", font=("Verdana",  15, "normal"))
            if bluepos>=30:
                blue.write("Winner!", font=("Verdana",  15, "normal")) 
                yellow.write("Winner!", font=("Verdana",  15, "normal"))
            flag=flag*(-1)   
def dicerollblue():
    global blueroll,bluepos,flag
    while yellowpos<30 and bluepos<30 and flag==-1:
            blueroll=random.randint(1,6)
            bluego=[]
            for j in range(bluepos+1,bluepos+blueroll+1):
                bluego.append(j)  
            for i in bluego:
                if i<=30:
                    blue.goto(d[i][0],d[i][1])   
                    bluepos=bluepos+1
                else:
                    break
            if ladder(bluepos)!=0:
                blue.goto(d[ladder(bluepos)][0],d[ladder(bluepos)][1])
                bluepos=ladder(bluepos)
            if snake(bluepos)!=0:
                blue.goto(d[snake(bluepos)][0],d[snake(bluepos)][1])
                bluepos=snake(bluepos)     
            if yellowpos>=30:
                    yellow.write("Winner!", font=("Verdana",  15, "normal"))
                    blue.write("Loser!", font=("Verdana",  15, "normal"))
            if bluepos>=30:
                    yellow.write("Loser!", font=("Verdana",  15, "normal"))
                    blue.write("Winner!", font=("Verdana",  15, "normal"))
            flag=flag*(-1)            
turtle.listen()
turtle.onkey(dicerollyellow,'Down')
turtle.onkey(dicerollblue,'Up')                      
turtle.mainloop()  
#%%  
