from tkinter import Tk, Label, Button, RAISED

root1 = Tk()

# Define the widgets outside the functions for global access
l1 = Button(root1, text="Button 1", bg="#000b1f", height=3, command=lambda: print("Button 1"), relief=RAISED, bd=0)
l2 = Button(root1, text="Close", bg="#09f6ff", command=root1.quit, height=3, width=15, relief=RAISED, bd=0)
l3 = Button(root1, text="Female voice", bg="#09f6ff", command=lambda: print("Female voice"), height=3, width=15, relief=RAISED, bd=0)
l4 = Button(root1, text="More Options", bg="#09f6ff", height=3, width=15, relief=RAISED, bd=0, command=lambda: clear_buttons())
l5 = Label(root1, text="Image", bg="black", relief=RAISED, bd=0)

# Additional labels and buttons
label = Label(root1, text="Created by Rithvik", fg="blue", bg="black", relief=RAISED)
button_back = Button(root1, text="<---Back", bg="#09f6ff", height=3, width=15, relief=RAISED, bd=0, command=lambda: place_buttons())

def clear_buttons():
    buttons_to_forget = (l1, l2, l3, l4)
    for widget in buttons_to_forget:
        widget.place_forget()
    label.place(x=250, y=80)
    button_back.place(x=250, y=120)

def place_buttons():
    buttons_to_place = (l1, l2, l3, l4, l5)
    for widget in buttons_to_place:
        widget.place()
    label.place_forget()
    button_back.place_forget()

# Initial placement
l1.place(x=243, y=50)
l2.place(x=100, y=50)
l3.place(x=100, y=105)
l4.place(x=100, y=155)
l5.pack()

root1.mainloop()
