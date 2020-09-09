# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:04:44 2020

@author: lenovo
"""

from tkinter import *


root = Tk()

def intro():


  topFrame = Frame(root)
  topFrame.pack()
  bottomFrame = Frame(root)
  bottomFrame.pack(side = BOTTOM)

  photo = PhotoImage(file="hg.tif")
  label = Label(root, image=photo)
  label.pack(side = TOP)

  t = Text(wrap=WORD, height = 10)
  t.insert(INSERT, "This is the first screen")
  t.insert(END, "")
  t.pack()

  # button 1 here should take us to the second screen
  button1 = Button(bottomFrame, text="Option 1", fg="black", command=chapter2)
  button2 = Button(bottomFrame, text="Option 2", fg="black")
  button3 = Button(bottomFrame, text="Option 3", fg="black")

  button1.pack(side = LEFT)
  button2.pack(side = LEFT)
  button3.pack(side = LEFT)

  root.mainloop()


def chapter2():


  topFrame = Frame(root)
  topFrame.pack()
  bottomFrame = Frame(root)
  bottomFrame.pack(side = BOTTOM)

  photo1 = PhotoImage(file="hg.tif")
  label1 = Label(root, image=photo1)
  label1.pack(side = TOP)

  t1 = Text(wrap=WORD)
  t1.insert(INSERT, "This is the second screen")
  t1.insert(END, "")
  t1.pack()

  button4 = Button(bottomFrame, text="this", fg="black")
  button5 = Button(bottomFrame, text="that", fg="black")
  button6 = Button(bottomFrame, text="the other", fg="black")

  button4.pack(side = LEFT)
  button5.pack(side = LEFT)
  button6.pack(side = LEFT)

  root.mainloop()

intro()