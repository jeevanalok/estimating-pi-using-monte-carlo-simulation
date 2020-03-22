"""
this is python program to estimate the value of pi using monte carlo simulation.

pseudocode:-
->a circle of radius r is inscribed in a square whose side is 2r
->points of random (x,y) values are generated and the points falling inside the circle are kept tracked of
->algortihm
    (*)area of circle=no. of points inside circle=pi*r*r
    (*)area of sqaure=total points= 2r *2r
    (*)dividing both we get, pi=4*(no.of points in circle/total points)

For interactive simulation, tkinter module is used.
dt of completion=22 march 2020
"""

#importing necessary modules
import tkinter as tk
import random

#creating window
window=tk.Tk()
window.geometry("720x720")
window.title("estimate_pi")
window.config(bg="#3866d1")


total_points=0      #total points
in_points=0         #no.of points in circle

#creating canvas and the inscribed circle in a sqaure
sketch=tk.Canvas(window,width=500,height=475,bg="white")
sketch.place(relx=0.5,rely=0.5,anchor="center")
sketch.create_rectangle(100,100,400,400,outline="black",width=3) #side of square=400-100=300
sketch.create_oval(100,100,400,400,outline="black",width=2)     #radius of circle=300/2=150

radius=150  #radius of circle

#function to get total points from current value of slider
def get_total_points(value):
    global total_points
    total_points=scale.get()
    start_simulation()
    
#function to start simulation
def start_simulation():    
#reseting the canvas
    sketch.create_rectangle(100,100,400,400,outline="black",width=3,fill="#FFFFFF")
    sketch.create_oval(100,100,400,400,outline="black",width=2,fill="#FFFFFF")
#redrawing the circle in square
    sketch.create_rectangle(100,100,400,400,outline="black",width=3)
    sketch.create_oval(100,100,400,400,outline="black",width=2)

#initialising in_points to 0
    in_points=0
#loop to generate random (x,y) points    
    for dots in range(total_points):
        x=random.randint(103,394)
        y=random.randint(103,394)
        #center of circle =(250,250)
        x1=x-250
        y1=y-250
#using distance formula for 2 points
        distance=(x1**2+y1**2)**0.5

#making points green if they are in circle
        if distance<radius:
            sketch.create_oval(x,y,x+4,y+4,fill="green",outline="green",width="0.5")
            in_points+=1

#making points red if they fall outside circle
        elif distance>radius:
            sketch.create_oval(x,y,x+4,y+4,fill="red",outline="red",width="0.5")

#calculating value of pi
    pi=4*(in_points/total_points)

#creating labels
    pi_label=tk.Label(window,text="value of pi is: "+str(pi),fg="#3866d1",font=("courier",12)).grid(row=0,column=0)
    in_point_label=tk.Label(window,text=" points in circle: "+str(in_points),fg="#3866d1",font=("courier",12)).grid(row=1,column=0)

#creating scale slider and other additional widgets
instruction=tk.Label(window,text="drag the slider to control the number of points",font=("times",10))
instruction.place(relx=0.5,rely=0.9,anchor="s")
scale=tk.Scale(window,from_=0,to=2000,orient="horizontal",length=450,tickinterval=500,command=get_total_points)
scale.place(relx=0.5,rely=0.825,anchor="s")
quit_button=tk.Button(window,text="quit",command=window.destroy,fg="red")
quit_button.place(relx=0.5,rely=0.95,anchor="s")


window.mainloop()