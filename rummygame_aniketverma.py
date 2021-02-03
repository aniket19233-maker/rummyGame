from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random
import time

root = Tk()


canv = Canvas(root, width=1400, height=1000, bg='Green')
canv.grid(row=2, column=3)
canv.pack()

imge = ImageTk.PhotoImage(Image.open("/Users/aniketverma/Desktop/cards/back_side.pbm").resize((100,100),Image.ANTIALIAS))  # PIL solution
image=canv.create_image(700, 250, anchor=NW, image=imge)


'''
img = ImageTk.PhotoImage(Image.open("/Users/aniketverma/Desktop/cards/heart_Ac.pbm").resize((100,100),Image.ANTIALIAS))  # PIL solution
imege=canv.create_image(250, 150, anchor=NW, image=img)

canv.itemconfig(image,image=img)
canv.itemconfig(imege,image=imge)

'''


def check_seq():
            for i in range(9):
                for j in range(3):
                    if d[j]==d[j+1] and d[j+1]==d[j+2]:
                        canv.create_text(500,10,fill="darkblue",font="Times 20 italic bold",text="we identified a sequence.good job!")
                        canv.update()
                        break
                i += (j+2)

r=[32,33,34,89]
for i in range(3):
    r[i] = ImageTk.PhotoImage(Image.open("/Users/aniketverma/Desktop/cards/back_side.pbm").resize((100,100),Image.ANTIALIAS))  # PIL solution
    canv.create_image(300 + 30*i, 250, anchor=NW, image=r[i])
    lis = ["heart", "clubs", "diamonds","spades"]
    lst=["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    k=random.choice(lis)
    e=random.choice(lst)
    iu=ImageTk.PhotoImage(Image.open("/Users/aniketverma/Desktop/cards/" + k+ "_" + e + "c" + ".pbm").resize((100,100),Image.ANTIALIAS))  # PIL solution
    canv.create_image(390, 250, anchor=NW, image=iu)
    iut=canv.create_image(390, 250, anchor=NW, image=iu)
    
    
p=[]

for i in range(10):
    #lis = list("heart", "clubs", "diamonds", "spades")
    #lst=["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    lis = ["heart", "clubs", "diamonds","spades"]
    #lis= lis.split()
    lst=["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    a=random.choice(lis)
    b=random.choice(lst)
    p.append("/Users/aniketverma/Desktop/cards/" + a + "_" + b + "c" + ".pbm")
    #img = ImageTk.PhotoImage(Image.open("/Users/aniketverma/Desktop/cards/" + a + "_" + b + "c" + ".pbm").resize((100,100),Image.ANTIALIAS))  # PIL solution
    #canv.create_image(10+100*i, 10, anchor=NW, image=img)

t=["c","d","e","f","g","h","i","j","k","l"]
d=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(p)):
    t[i] = ImageTk.PhotoImage(Image.open(p[i]).resize((100,100),Image.ANTIALIAS))  # PIL solution
    canv.create_image(100 + 100*i + 10*i ,500, anchor=NW, image=t[i])
    d[i]=canv.create_image(100 + 100*i + 10*i ,500, anchor=NW, image=t[i])


y=[]

for i in range(10):
    lis = ["heart", "clubs", "diamonds","spades"]
    lst=["A","2","3","4","5","6","7","8","9","10","J","K","Q"]
    a=random.choice(lis)
    b=random.choice(lst)
    y.append("/Users/aniketverma/Desktop/cards/" + a + "_" + b + "c" + ".pbm")

q=["c","d","e","f","g","h","i","j","k","l"]
h=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(y)):
    q[i] = ImageTk.PhotoImage(Image.open(y[i]).resize((100,100),Image.ANTIALIAS))  # PIL solution
    canv.create_image(100 + 100*i + 10*i ,10, anchor=NW, image=q[i])
    h[i]=canv.create_image(100 + 100*i + 10*i ,10, anchor=NW, image=q[i])


player1=True
player2 = False

global j
j=0

while j!=1:
    while player1:
        canv.create_text(100,200,fill="darkblue",font="Times 20 italic bold",text="PLAYER1")        
        canv.update()
        global u
        u=0
        global l
        l=""


        def move(event):
            global u
            global l
            move_list=['D','P']
            number=['0','1','2','3','4','5','6','7','8','9']
            l+=event.char
            print(l)
            if l[0] =="D" and l[1] in number:
                canv.move(d[int(l[1])] ,(390-canv.coords(d[int(l[1])])[0]),-250)
                canv.delete(d[int(l[1])])
                root.update()
                l=""
                check_seq()
            if l[0] == 'P' and l[1] in number and l[2] in number :
                canv.itemconfig(d[int(l[1])],image=t[int(l[2])])
                canv.itemconfig(t[int(l[2])],image = d[int(l[1])])
                root.update()
                l=""
                check_seq()
            if event.char == "1":
                co=canv.coords(d[0])
                canv.create_rectangle(co[0],co[1],co[0]+100,co[1]+100,fill="Green")
                canv.move(d[0],700 -co[0],250 - co[1])
                #co=canv.coords(d[0])
                #canv.create_rectangle(co[0],co[1],co[0]+100,co[1]+100,fill="Green")
                #canv.itemconfig(d[0],state="hidden")
                root.update()
            l=""
                
                
        root.bind("<Key>", move)

        player1 = False
        player2 = True
    if(len(number)==0):
        j=0
        
    

    while(player2):
        canv.create_text(100,200,fill="darkblue",font="Times 20 italic bold",text="PLAYER2")
        canv.update()
        global g
        g=0
        global s
        s=""

        def move(event):
            global g
            global s
            move_lists=['U','Q']
            numbers=['0','1','2','3','4','5','6','7','8','9']
            s+=event.char
            print(s)
            if s[0] =="U" and s[1] in numbers:
                canv.move(h[int(l[1])] ,(390-canv.coords(h[int(s[1])])[0]),250)
                canv.delete(h[int(l[1])])
                root.update()
                s=""
                check_seq()
            if s[0] == 'Q' and s[1] in number and s[2] in number :
                canv.itemconfig(h[int(s[1])],image=q[int(s[2])])
                canv.itemconfig(q[int(s[2])],image = h[int(s[1])])
                root.update()
                s=""
                check_seq()
            if event.char == "1":
                cos=canv.coords(h[0])
                canv.create_rectangle(cos[0],cos[1],cos[0]+100,cos[1]+100,fill="Green")
                canv.move(h[0],700 -cos[0],250 - cos[1])
                number.pop(0)
                #co=canv.coords(d[0])
                #canv.create_rectangle(co[0],co[1],co[0]+100,co[1]+100,fill="Green")
                #canv.itemconfig(d[0],state="hidden")
                root.update()
                
                
        root.bind("<Key>", move)
        player2 = False
        player1 = True

    if(len(numbers)==0):
        j=0
        

root.mainloop()

