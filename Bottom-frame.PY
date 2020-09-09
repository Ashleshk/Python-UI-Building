from tkinter import filedialog ,Frame
from tkinter import *
from tkinter import messagebox


from PIL import Image,ImageTk
window= Tk()
window.title("vtvjrejeyeyjkerke ry ryr")
window.geometry('1200x725')
global file
 

def browse():

    file= filedialog.askopenfilename(initialdir="/",title="select image",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    img= Image.open(file)
    render=ImageTk.PhotoImage(img)
    img=Label(window,image=render)
    img.image=render
    img.place(x=170,y=10)

def out():
    messagebox.showinfo("output","AAnkh dikhata hai madarjaaat")

btn1=Button(window, text="select image", command=browse)
btn1.config(height=3,width=20)
btn1.place(x=375, y=650)

btn2=Button(window, text="Test",command=out)
btn2.config(height=3,width=20)
btn2.place(x=675, y=650)

btn3=Button(window, text="Result", command=window.destroy)
btn3.config(height=3,width=20)
btn3.place(x=950,y=650)

window.mainloop()