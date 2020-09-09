# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:28:07 2020

@author: lenovo
"""
from tkinter import *

root= Tk()
root.title("vtvjrejeyeyjkerke ry ryr")
root.geometry('1200x725')

def createFrames(self):
    #Main Upper Frame
    topFrame = Frame(height=120, width=800, bd=1, relief=SUNKEN)
    topFrame.pack(side=TOP)

    #Left Frame in Main Upper Frame
    topFrameLeft = Frame(topFrame, height=120, width=400)
    topFrameLeft.pack(side=LEFT)

    #Right Frame in Main Upper Frame
    topFrameRight = Frame(topFrame, height=120, width=400)
    topFrameRight.pack(side=RIGHT)

    #Frame for GPS, Lower
    centerFrame = Frame(width=800, height=400, bg="",
                        colormap="new",bd=3, relief=GROOVE)
    centerFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

    #photo stuff
    photo = PhotoImage(file="hg.png")
    #scale_w = 3
    #scale_h = 400/200
    #photo = photo.zoom(scale_w, scale_h)
    #photo = photo.subsample(1)
    Image_Label = Label(centerFrame, image=photo)
    Image_Label.photo = photo
    Image_Label.pack(fill=BOTH, expand=True)

    #Label for Left Frame
    Left_Label = Label(topFrameLeft, width=56, text="Audio", bg="gray",
                       fg="blue")
    Left_Label.pack()

    #Label for Right Frame
    Right_Label = Label(topFrameRight, width=60,
                        text="Phone/Notification",
                        bg="Green", fg="Black")
    Right_Label.pack()
createFrames(root)
root.mainloop()