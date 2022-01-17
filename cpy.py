from tkinter import *

def CYW():
    root = Tk()
    root.title("check your wifi")
    root.config(bg="black")

    ph = PhotoImage(file="C:/Users/LENOVO/Downloads/Jarvis.HP-jarvis.v1/Jarvis.HP-jarvis.v1/im.png")

    Label(root, image=ph,bg="black").pack()

    root.mainloop()