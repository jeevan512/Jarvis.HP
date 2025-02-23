from tkinter import *
from PIL import Image, ImageTk
from jarvis import jarvisimages

def more_options():
    root = Tk()
    root.title("More Options")
    root.config(background="black")
    sb = PhotoImage(file="jarvis start bt.png") # keep this PhotoImage

    #root.icon1 = ImageTk.PhotoImage(Image.open("PIC.png"))
    #root.iconphoto(False, root.icon1)

    Label(root, image=jarvisimages, bg="black").pack()


    root.mainloop()

def gte():
    l2.place(x=100, y=50)
    l1.place(x=243, y=50)
    l3.place(x=100, y=105)
    l4.place(x=100, y=155)
    l5.pack()

    l11.forget_place()
    b11.forget_place()

more_options()