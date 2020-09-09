from tkinter import filedialog ,Frame
from tkinter import *
from tkinter import messagebox
from utils.menu import create_Menu
from PIL import ImageTk,Image
global file
# ----------------------------centre positioning of main-window----------------
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d-%d-%d' % (width, height, x, y))
#-------------------------------------------------------------------------
def browse():

    file= filedialog.askopenfilename(initialdir="/",title="select image",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    img= Image.open(file)
    render=ImageTk.PhotoImage(img)
    img=Label(root,image=render)
    img.image=render
    img.place(x=170,y=10)

def out():
    messagebox.showinfo("output","AAnkh dikhata hai madarjaaat")

#------------------  PUTTING IT ALL TOGETHER ----------------------------------
root = Tk()
root.title("VEHICLE DETECTION")
center_window(1200,725)
root.configure(bg='#CDDC39')
root=create_Menu(root)

# ------------   SIDE PANEL----------------------------------------------
button1 = Button(root, text="HOG+SVM", fg="red",height=5,width=20)
button2 = Button(root, text="HOG+LOG", fg="red",height=5,width=20)
button3 = Button(root, text="CNN", fg="red",height=5,width=20)
button4 = Button(root, text="FRCNN", fg="red",height=5,width=20)
button5 = Button(root, text="RESULTS", fg="red",height=5,width=20)
button1.place(x=0,y=10)
button2.place(x=0,y=100)
button3.place(x=0,y=190)
button4.place(x=0,y=280)
button5.place(x=0,y=370)

btn1=Button(root, text="select image", command=browse)
btn1.config(height=3,width=20)
btn1.place(x=375, y=650)

btn2=Button(root, text="Test",command=out)
btn2.config(height=3,width=20)
btn2.place(x=675, y=650)

btn3=Button(root, text="Result", command=root.destroy)
btn3.config(height=3,width=20)
btn3.place(x=950,y=650)
 
root.mainloop()