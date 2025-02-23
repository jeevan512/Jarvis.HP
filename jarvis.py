# import all modules
import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import datetime as dt
import random
import pyjokes as pj
from tkinter import *
import time
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
import sys
import os

lis = sr.Recognizer()
friend = pyttsx3.init()

"""RATE"""
rate = friend.getProperty('rate')  # getting details of current speaking rate
friend.setProperty('rate', 150)  # setting up new voice rate


def fmv():
    """VOICE"""
    voicess = friend.getProperty('voices')  # getting details of current voice
    friend.setProperty('voice', voicess[0].id)  # changing index, changes voices. 1 for female
    speak("changed to male voice sir")

    Button(root1, text="female voice", bg="#09f6ff", command=fv, height=3, width=15, relief=RAISED, bd=0).place(
        x=100, y=105)


def fv():
    """VOICE"""
    voices = friend.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    friend.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    speak("changed to femail voice sir")

    btuns = Button(root1, text="male voice", bg="#09f6ff", command=fmv, height=3, width=15, relief=RAISED, bd=0).place(
        x=100, y=105)


def speak(text):
    friend.say(text)
    friend.runAndWait()


speak("hello this is jarvis the assistant of rithvik")

try:
    import pywhatkit as py
    import wikipedia as wi

    root1 = Tk()
    root1.title("Jarvis")
    global icon
    icon = PhotoImage(file="PIC.png")
    root1.geometry("600x300")
    root1.attributes("-alpha", 9.0)
    root1.iconphoto(False, icon)
    root1.config(bg="black")  # Happy.root
    global jarvisimages
    jarvisimages = PhotoImage(file="jarvis start bt.png")
    jbt = PhotoImage(file="Untitled.png")
    root1.attributes("-alpha", 0.7)


    def aiJ():
        def command():
            with sr.Microphone() as source:
                try:
                    audio = lis.listen(source)
                    test = lis.recognize_google(audio)
                    test = test.lower()
                    test = test.replace("jarvis", "")
                    if "youtube" in test:
                        speak("opening youtube mam or sir")
                        url = "www.youtube.com"
                        wb.get().open_new(url)
                    elif "joke" in test:
                        speak(pj.get_joke())
                        print(pj.get_joke())
                    elif "gaming" in test:
                        speak("opening td gaming sir")
                        url = "https://www.youtube.com/c/TeluguDostGaming"
                        wb.get().open_new(url)
                    elif "time" in test:
                        times = dt.datetime.now().strftime("%I:%M %p")
                        speak(times)
                    elif "dashboard" in test:
                        #sys2()
                        speak("ok sir")
                    elif "play" in test:
                        speak("playing it sir")
                        py.playonyt(test)
                    elif "search for" in test:
                        test = test.replace("search for", "")
                        speak("searching for" + test)
                        py.search(test)
                    elif "who is" in test:
                        test = test.replace("who is", "")
                        info = wi.summary(test, 2)
                        print(info)
                        speak(info)
                    elif "python index" in test:  # nar prodect{GTAS5="kimopoli"}
                        speak("opening python module installer")
                        url = "https://pypi.org/"
                        wb.get().open_new(url)
                    elif "rockstar" in test:
                        speak("opening gta5 sir")
                        os.startfile(r"C:\Users\innug\Downloads\Grand Theft Auto V\GTAVLauncher.exe")
                    elif "video editor" in test:
                        speak("opening video editor sir")
                        os.startfile(
                            r"C:\Users\innug\AppData\Local\Wondershare\Wondershare Filmora\Wondershare Filmora Launcher.exe")
                    elif "google.com" in test:
                        speak("opening google sir")
                        url = "www.google.com"
                        wb.get().open_new(url)
                    elif "facebook" in test:
                        speak("opening facebook sir")
                        url = "www.facebook.com"
                        wb.get().open_new(url)
                    elif "whatsapp" in test:
                        speak("opening whatsapp sir")
                        url = "https://web.whatsapp.com/"
                        wb.get().open_new(url)
                    elif "instagram" in test:
                        speak("opening instagram sir")
                        url = "https://www.instagram.com/"
                        wb.get().open_new(url)
                    elif "cosmic boy" in test:
                        speak("opening the cosmic boy youtube channel sir")
                        url = "https://www.youtube.com/c/TheCosmicBoy1"
                        wb.get().open_new(url)
                    elif "cosmic 2" in test:  # HI impoirt  tkinter code=KJIHHJIKewLOPERGJIP@@RIP=instant code of buf gaming app cosmic youtube channel code = wb.Get().new(url).js.py.oot.optb webbroser code = .l::::::olk:::alk
                        speak("opening the cosmic boy 2.0 sir")
                        url = "https://www.youtube.com/c/TheCosmicBoy20"  # the url link of cosmic boy 2.0
                        wb.get().open_new(url)  # cosmic boy 2 gaming youtube channel in the language of telugu
                    elif "hello" or "hi" or "hey" in test:
                        speak(
                            "hello sir or mam this is jarvis a basic ai and my boss is rithvik and is there anything that i can help to you")
                    elif "quit" in test:

                        shud()
                    elif "ananya" in test:
                        speak("she is a bad girl")
                        print("she is a bad girl")
                    else:
                        pass


                except:
                    pass

        while True:
            command()


    def shud():
        messagebox.showinfo("", "do you want to close AI jarvis")
        root1.destroy()


    global lable
    global babble

    text = ("The program is created by rithvik")
    text2=("for any questions or errors contact for number")
    text3= ("number is 7013259413")


    def clear_buttons():
        buttons_to_forget = (l1, l2, l3, l4)
        for widget in buttons_to_forget:
            widget.place_forget()
        global label
        global label1
        global label2  # Ensure label is declared as global
        global babble  # Ensure babble is declared as global
        label = Label(root1, text=text, fg="blue", bg="#000B1F", relief=RAISED, bd=0)
        label.place(x=250, y=80)
        label1 = Label(root1, text=text2, fg="blue", bg="#000B1F", relief=RAISED, bd=0)
        label1.place(x=220, y=100)
        label2 = Label(root1, text=text3, fg="blue", bg="#000B1F", relief=RAISED, bd=0)
        label2.place(x=250, y=120)

        babble = Button(root1, text="<---Back", bg="#09f6ff", height=1, width=9, relief=RAISED, bd=0, command=gte)
        babble.place(x=100, y=60)


    def gte():
        label.place_forget()
        label1.place_forget()
        label2.place_forget()
        babble.place_forget()  # Correct method call

        l1.place(x=243, y=50)
        l2.place(x=100, y=50)
        l3.place(x=100, y=105)
        l4.place(x=100, y=155)  # Updated y-coordinate to avoid overlap with l3
        l5.pack()


    l5 = Label(root1, image=jarvisimages, width=600, bg="black", relief=RAISED, bd=0)
    l5.pack()  # Pack l5

    l1 = Button(root1, image=jbt, bg="#000b1f", height=180, command=aiJ, relief=RAISED, bd=0)
    l1.place(x=243, y=50)

    l2 = Button(root1, text="close", bg="#09f6ff", command=shud, height=3, width=15, relief=RAISED, bd=0)
    l2.place(x=100, y=50)

    l3 = Button(root1, text="Female voice", bg="#09f6ff", command=fv, height=3, width=15, relief=RAISED, bd=0)
    l3.place(x=100, y=105)

    l4 = Button(root1, text="More Options", bg="#09f6ff", height=3, width=15, relief=RAISED, bd=0,
                command=clear_buttons)
    l4.place(x=100, y=155)

    root1.mainloop()
except:
    pass
    # CYW()