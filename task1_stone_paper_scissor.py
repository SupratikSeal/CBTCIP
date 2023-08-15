from tkinter import *
import random
root=Tk()

#Main Functions 

def rock():     #Event handling for rock
    list=["rock","paper","scissor"]
    c=random.choice(list)
    a="rock"
    e.config(text="Computer : " +c)

    if c==a:
        f.config(text="Result : Draw")
    elif c=="rock" and a=="paper":
        f.config(text="Result : You won",fg="Green")
    elif c=="rock" and a=="scissor":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="rock":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="scissor":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="rock":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="paper":
        f.config(text="Result : Computer won")

def paper():   #Event handling for paper
    list=["rock","paper","scissor"]
    c=random.choice(list)
    a="paper"
    e.config(text="Computer : " +c)


    if c==a:
        f.config(text="Result : Draw")
    elif c=="rock" and a=="paper":
        f.config(text="Result : You won")
    elif c=="rock" and a=="scissor":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="rock":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="scissor":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="rock":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="paper":
        f.config(text="Result : Computer won")

def scissor():   #Event handling for scissor
    list=["rock","paper","scissor"]
    c=random.choice(list)
    a="scissor"
    e.config(text="Computer : " +c)


    if c==a:
        f.config(text="Result : Draw")
    elif c=="rock" and a=="paper":
        f.config(text="Result : You won")
    elif c=="rock" and a=="scissor":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="rock":
        f.config(text="Result : Computer won")
    elif c=="paper" and a=="scissor":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="rock":
        f.config(text="Result : You won")
    elif c=="scissor" and a=="paper":
        f.config(text="Result : Computer won")





#GUI management ---
root.title("Rock Paper Scissor")
root.geometry("300x200")
d=Label(root,text="Rock Paper Scissor Game",font="Ariel 20",fg="Red")
d.pack()
a=Label(root,text="Choose below :")
a.pack()
b=Button(root,text="Rock",command=rock)
b.pack()
c=Button(root,text="Paper",command=paper)
c.pack()
c=Button(root,text="Scissor",command=scissor)
c.pack()
e=Label(root)  #For dispaling what computer choose
e.pack()
f=Label(root,fg="Green") #For displaying wining result 
f.pack()
root.mainloop()
