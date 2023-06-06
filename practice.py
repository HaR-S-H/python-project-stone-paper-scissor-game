from tkinter import*
from PIL import Image,ImageTk
from random import randint
from pygame import mixer
def action():
    name=e1.get()
    window=Toplevel()
# window.wm_attributes('-transparentcolor','white') 
    window.title("Rock Paper Scissors Game")
    img=Image.open("1847.png")
    size=img.resize((1400,725),Image.LANCZOS)
    nimg=ImageTk.PhotoImage(size)
    label=Label(window,image=nimg)
    label.place(x=0,y=0)
# window.configure(background="green")
    window.geometry("5000x5000")

    image_rock1=ImageTk.PhotoImage(Image.open("rock1.jpg"))
    image_paper1=ImageTk.PhotoImage(Image.open("paper1.jpg"))
    image_scissor1=ImageTk.PhotoImage(Image.open("scissor1.jpg"))
    image_rock2=ImageTk.PhotoImage(Image.open("rock2.jpg"))
    image_paper2=ImageTk.PhotoImage(Image.open("paper2.jpg"))
    image_scissor2=ImageTk.PhotoImage(Image.open("scissor2.jpg"))

    label_player=Label(window,image=image_scissor1)
    label_computer=Label(window,image=image_scissor2)
    label_computer.grid(row=2,column=0)
    label_player.grid(row=2,column=4)

    rou=Label(window,text="Round",font=("arial",60,"bold"),fg="red")
    round=Label(window,text=1,font=("arial",60,"bold"),fg="red")
    computer_score=Label(window,text=0,font=("arial",60,"bold"),fg="red")
    player_score=Label(window,text=0,font=("arial",60,"bold"),fg="red")
    rou.grid(row=0,column=2)
    round.grid(row=0,column=3)
    computer_score.grid(row=2,column=1)
    player_score.grid(row=2,column=3)

    player_indicator=Label(window,font=("arial",40,"bold"),text=name,bg="orange",fg="blue")
    computer_indicator=Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="orange",fg="blue")
    computer_indicator.grid(row=1,column=0)
    player_indicator.grid(row=1,column=4)

    final_message=Label(window,font=("arial",40,"bold"),bg="red",fg="white")
    final_message.grid(row=4,column=2)

    def reset():
        round["text"]=1
        player_score['text']=0
        computer_score["text"]=0
        final_message["text"]=""
        button_rock['state']=NORMAL
        button_paper['state']=NORMAL
        button_scissor['state']=NORMAL
        play_again["state"]=DISABLED


    def updateMessage(a):
        final_message['text']=a
        button_rock['state']=DISABLED
        button_paper['state']=DISABLED
        button_scissor['state']=DISABLED
        play_again['state']=NORMAL

    def Computer_Update():
        final=int(computer_score['text'])
        final+=1
        computer_score['text']=str(final)
        r=int(round['text'])
        r+=1
        round['text']=str(r)

    def Player_Update():
        final=int(player_score['text'])
        final+=1
        player_score['text']=str(final)
        r=int(round['text'])
        r+=1
        round['text']=str(r)

    def winner_check(p,c):
        if p==c:
            # updateMessage("It's a tie")
            r=int(round['text'])
            r+=1
            round['text']=str(r)
        elif p=="rock":
            if c=="paper":
                # updateMessage("Computer Wins!!")
                Computer_Update()
            else:
                # updateMessage("Player Wins!!")
                Player_Update()
        elif p=="paper":
            if c=="scissor":
                # updateMessage("Computer Wins!!")
                Computer_Update()
            else:
                # updateMessage("Player Wins!!")
                Player_Update()
        elif p=="scissor":
            if c=="rock":
                # updateMessage("Computer Wins!!")
                Computer_Update()
            else:
                # updateMessage("Player Wins!!")
                Player_Update()

        r=int(round['text'])
        if(r==6):
            ps=int(player_score["text"])
            cs=int(computer_score["text"])
            if(ps>cs):
                updateMessage("Player Wins!!")
            elif(cs>ps):
                updateMessage("Computer Wins!!")
            else:
                updateMessage("It's a Tie")
            round["text"]=5


    to_select=["rock","paper","scissor"]

    def choice_update(a):
        choice_computer=to_select[randint(0,2)]
        if choice_computer=="rock":
            label_computer.configure(image=image_rock2)
        elif choice_computer=="paper":
            label_computer.configure(image=image_paper2)
        else:
            label_computer.configure(image=image_scissor2)
    
        if a=="rock":
            label_player.configure(image=image_rock1)
        elif a=="paper":
            label_player.configure(image=image_paper1)
        else:
            label_player.configure(image=image_scissor1)

        winner_check(a,choice_computer)

    button_rock=Button(window,width=16,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock"),state=NORMAL)
    button_paper=Button(window,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper"),state=NORMAL)
    button_scissor=Button(window,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor"),state=NORMAL)
    button_rock.grid(row=3,column=1)
    button_paper.grid(row=3,column=2)
    button_scissor.grid(row=3,column=3)

    play_again=Button(window,width=10,height=2,font=("arial",10,"bold"),bg="yellow",fg="red",text="Play again",command=reset,state=DISABLED)
    play_again.grid(row=7,column=1,sticky=EW)
    e=Button(window,width=10,height=2,font=("arial",10,"bold"),bg="yellow",fg="red",text="Exit",command=lambda:window.destroy())
    e.grid(row=7,column=3,sticky=EW)


    window.mainloop()

root=Tk()
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
def music():
    mixer.init()
    mixer.music.load('song.mp3')
    mixer.music.play()
img1=Image.open("bg1.jpg")
size=img1.resize((1400,725),Image.LANCZOS)
nimg=ImageTk.PhotoImage(size)
label=Label(root,image=nimg)
label.place(x=0,y=0)
title=Label(root,font=("arial",40,"bold"),text="ROCK PAPER SCISSORS",bg="black",fg="white")
title.place(x=375,y=250)
# root.geometry("300x200")
root.configure(background="green")
root.title("Rock Paper Scissors Game")
# root.maxsize(300,200)
# root.minsize(300,200)
l1=Label(root,text="Enter player name : ",font="time 20 bold",fg="white",bg="black")
l1.place(x=400,y=400)
e1=Entry(root,width=50,bd=10)
e1.place(x=700,y=400)
button=Button(root,text="Play Game",width=10,fg="white",bg="magenta",font="time 10 bold",command=action)
button.place(x=650,y=500)
button=Button(root,text="Quit Game ",width=10,fg="white",bg="magenta",font="time 10 bold",command=root.destroy)
button.place(x=650,y=550)
button=Button(root,text="music on",width=10,fg="white",bg="magenta",font="time 10 bold",command=music)
button.place(x=250,y=550)
button=Button(root,text="music off",width=10,fg="white",bg="magenta",font="time 10 bold",command=mixer.music.stop)
button.place(x=1000,y=550)
root.mainloop()