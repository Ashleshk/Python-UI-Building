from tkinter import *
from PIL import ImageTk,Image

def doNothing():
    print("VEHICLE DETECTION")
#centre positioning of main-window
def center_window(width,height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d-%d-%d' % (width, height, x, y))
    
    
#open results window
def open_window():
    top = Tk()
    topp=Frame(top)
    topp.pack()
    topp.geometry('1200x725')
    topp.configure(bg='#ff7700')
    top.title("RESULTS...!!!!!")
    button9 = Button(topp, text="HOG+SVM", fg="red",command=open_table1)
    button9.pack()
    button10 = Button(topp, text="HOG+LOG", fg="red",command=open_table2)
    button10.pack()
    button11 = Button(topp, text="CNN", fg="red")
    button11.pack()
    button12 = Button(topp, text="FRCNN", fg="red")
    button12.pack()
    topp.pack(side=LEFT)
def open_table1():
    top = Tk()
    top.title("HOG RESULTS")
    l1 = Label(top, text="CAR")
    l1.grid(row=2, column=0)
    l1 = Label(top, text="PICK UP")
    l1.grid(row=3, column=0)
    l1 = Label(top, text="TRUCK")
    l1.grid(row=4, column=0)
    l1 = Label(top, text="UNMKOWN")
    l1.grid(row=5, column=0)
    l1 = Label(top, text="VAN")
    l1.grid(row=6, column=0)

    l1 = Label(top, text="HOG+SVM")
    l1.grid(row=0, column=1)

    l1 = Label(top, text="250")
    l1.grid(row=1, column=1)
    l1 = Label(top, text="500")
    l1.grid(row=1, column=2)

    l1 = Label(top, text="65.51")
    l1.grid(row=2, column=1)
    l1 = Label(top, text="62.49")
    l1.grid(row=3, column=1)
    l1 = Label(top, text="69.54")
    l1.grid(row=4, column=1)
    l1 = Label(top, text="69.54")
    l1.grid(row=5, column=1)
    l1 = Label(top, text="66.56")
    l1.grid(row=6, column=1)

    l1 = Label(top, text="72.52")
    l1.grid(row=2, column=2)
    l1 = Label(top, text="69.56")
    l1.grid(row=3, column=2)
    l1 = Label(top, text="64.54")
    l1.grid(row=4, column=2)
    l1 = Label(top, text="67.57")
    l1.grid(row=5, column=2)
    l1 = Label(top, text="63.53")
    l1.grid(row=6, column=2)

def open_table2():
    top = Tk()
    top.title("HOG RESULTS")
    l1 = Label(top, text="CAR")
    l1.grid(row=2, column=0)
    l1 = Label(top, text="PICK UP")
    l1.grid(row=3, column=0)
    l1 = Label(top, text="TRUCK")
    l1.grid(row=4, column=0)
    l1 = Label(top, text="UNMKOWN")
    l1.grid(row=5, column=0)
    l1 = Label(top, text="VAN")
    l1.grid(row=6, column=0)

    l1 = Label(top, text="HOG+LOGIST")
    l1.grid(row=0, column=1)

    l1 = Label(top, text="250")
    l1.grid(row=1, column=1)
    l1 = Label(top, text="500")
    l1.grid(row=1, column=2)

    l1 = Label(top, text="59.51")
    l1.grid(row=2, column=1)
    l1 = Label(top, text="62.54")
    l1.grid(row=3, column=1)
    l1 = Label(top, text="69.55")
    l1.grid(row=4, column=1)
    l1 = Label(top, text="58.53")
    l1.grid(row=5, column=1)
    l1 = Label(top, text="59.51")
    l1.grid(row=6, column=1)

    l1 = Label(top, text="65.57")
    l1.grid(row=2, column=2)
    l1 = Label(top, text="61.53")
    l1.grid(row=3, column=2)
    l1 = Label(top, text="68.54")
    l1.grid(row=4, column=2)
    l1 = Label(top, text="69.55")
    l1.grid(row=5, column=2)
    l1 = Label(top, text="70.62")
    l1.grid(row=6, column=2)


def open_img():
     canvas=Canvas(root,width=300,height=160)
     image=ImageTk.Photoimage(Image.open("C:\\Users\\Shruti\\Desktop\\BE PROJECT\\untitled\\images\\car.png"))
     canvas.create_image(0,0,anchor=NW,image=car)
     canvas.pack(side=RIGHT)

root = Tk()
root.title("VEHICLE DETECTION")
#root.geometry('1200x650')
center_window(1200,725)
root.configure(bg='#ff7700')
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Project", command=doNothing)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

subMenu = Menu(menu)
menu.add_cascade(label="Results", menu=subMenu)
subMenu.add_command(label="HOG+SVM", command=doNothing)
subMenu.add_command(label="HOG+LOG", command=doNothing)
subMenu.add_command(label="CNN", command=doNothing)
subMenu.add_command(label="FRCNN", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

subMenu = Menu(menu)
menu.add_cascade(label="Help", menu=subMenu)


topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
button1 = Button(topFrame, text="HOG+SVM", fg="red",height=5,width=20)
button2 = Button(topFrame, text="HOG+LOG", fg="red",height=5,width=20)
button3 = Button(topFrame, text="CNN", fg="red",height=5,width=20)
button4 = Button(topFrame, text="FRCNN", fg="red",height=5,width=20)
button5 = Button(topFrame, text="RESULTS", fg="red",height=5,width=20,command=open_window)

button6 = Button(bottomFrame, text="INPUT IMG", fg="red",command=open_img,height=5,width=23)
button7 = Button(bottomFrame, text="TEST", fg="red",height=5,width=23)
button8 = Button(bottomFrame, text="ACCURACY", fg="red",height=5,width=23)

button1.place(x=0,y=0)
button2.place(x=1,y=0)
button3.place(x=2,y=0)
button4.place(x=3,y=0)
button5.place(x=4,y=0)
button6.pack(side=LEFT)
button7.pack(side=LEFT)
button8.pack(side=LEFT)

topFrame.pack(side=LEFT)
bottomFrame.pack(side=BOTTOM)

root.mainloop()