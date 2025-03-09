import datetime as dt
import os
import webbrowser as wb
from typing import Any
import pyjokes as pj
import pyttsx3
import speech_recognition as sr
from pyttsx3 import Engine  
from tkinter import *
from tkinter import messagebox

questions = ["What is the capital of America?",
             "who was the first person to land on the moon",
             "What is the full form of NASA",
             "When did India get independence",
             "Who is the No.1 actor in India"]

ANswers = [" Washington"
          "Neel Armstrong"
          "National Aeronautics Space Administration"
          "1947"
          "Prabhas"]

lis = sr.Recognizer()
friend: Engine | Any = pyttsx3.init()


"""RATE"""
rate = friend.getProperty('rate')  # getting details of current speaking rate
friend.setProperty('rate', 150)  # setting up new voice rate

power_on = False  # Global variable to track power state

# Add this initialization at the start of your script
doe = None
doe1 = None



def fmv():
    """VOICE"""
    voicess = friend.getProperty('voices')  # getting details of current voice
    friend.setProperty('voice', voicess[0].id)  # changing index, changes voices. 1 for female
    speak("changed to jarvis sir")

    root1.title("Jarvis")

    global doe

    if doe:
        doe.place_forget()  # Hide the previous button if it exists

    doe = Button(root1, text="FRIDAY", bg="#09f6ff", command=fv, height=3, width=15, relief=RAISED, bd=0)
    doe.place(x=100, y=105)


def fv():
    """VOICE"""
    voices = friend.getProperty('voices')  # getting details of current voice
    friend.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    speak("changed to friday sir")

    global doe1

    if doe1:
        doe1.place_forget()  # Hide the previous button if it exists

    doe1 = Button(root1, text="JARVIS", bg="#09f6ff", command=fmv, height=3, width=15, relief=RAISED, bd=0)
    doe1.place(x=100, y=105)#get() if==="Bhavyesh"

    root1.title("Friday")

doe3 = ("infrastructure.plugin()int:"
        "get()")


def speak(int):
    friend.say(int)
    friend.runAndWait()

speak("hello this is jarvis the assistant of rithvik")

def ARGS_ifgtr():
    print("under score ___ detected")

    root = Tk()
    root.title("M.MAnish")

    MENUE = Tk()
    MENUE.title("rithvik")



    root.mainloop()
    MENUE.mainloop()

try:
    import pywhatkit as py
    import wikipedia as wi

    global root1

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
    jbt = PhotoImage(file="Untitiled.png")
    root1.attributes("-alpha", 0.7)




    def stopaij():
        global power_on
        power_on = False
        speak("Microphone stopped, sir.")

    def startaij():
        global power_on
        power_on = True
        speak("Microphone started, sir.")

    def comd():
        os.startfile(r"instructions.txt")
        #do the = External("Infra.get()")



    def aiJ():
        global power_on  # Use the global variable to track power state var.int()=="Bhavysh"

        def command():
            if not power_on:
                return  # Do nothing if power is off

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
                    elif "microphone" in test:
                        stopaij()
                    elif "start" in test:
                        startaij()
                    elif "zoom meeting" in test:
                        speak("opening zoom meeting")
                        os.startfile(r"C:\Users\innug\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom Workplace.lnk")
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
                        info = wi.summary(test, 2)#GET()
                        print(info)
                        speak(info)
                    elif "rithvik" in test:
                        speak("iohewdfuildsGGFIULg")
                    elif "python index" in test:
                        speak("opening python module installer")
                        url = "https://pypi.org/"
                        wb.get().open_new(url)
                    elif (""
                          "rockstar") in test:
                        speak("opening gta5 sir")
                        os.startfile(r"C:\Users\innug\Downloads\Grand Theft Auto V\GTAVLauncher.exe")
                    elif "video editor" in test:
                        speak("opening video editor sir")
                        os.startfile(r"C:\Users\innug\AppData\Local\Wondershare\Wondershare Filmora\Wondershare Filmora Launcher.exe")
                    elif "google" in test:
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
                    elif "instagram" in test:#ee.get(Z)
                        speak("opening instagram sir")
                        url = "https://www.instagram.com/"
                        wb.get().open_new(url)
                    elif "cosmic boy" in test:
                        speak("opening the cosmic boy youtube channel sir")
                        url = "https://www.youtube.com/c/TheCosmicBoy1"
                        wb.get().open_new(url)
                    elif "cosmic 2" in test:
                        speak("opening the cosmic boy 2.0 sir")
                        url = "https://www.youtube.com/c/TheCosmicBoy20"
                        wb.get().open_new(url)
                    elif "hello" or "hi" or "hey" in test:
                        speak("hello sir or mam this is jarvis a basic ai and my boss is rithvik and is there anything that i can help to you")
                    elif "quit" in test:
                        shud()
                    elif "ananya" in test:
                        speak("she is a bad girl")
                        print("she is a bad girl")
                    elif "module" in test:
                        speak("YOU FOOL")
                        ARGS_ifgtr()
                    else:
                        pass
                except:
                    pass

        if power_on:
            power_on = False
            speak("Powering off, sir.")
        else:
            power_on = True
            speak("Powering on, sir.")
            while power_on:
                command()

    def shud():
        messagebox.showinfo("", "do you want to close AI")
        root1.destroy()

    global label
    global babble

    text = "The program is created by rithvik"
    text2 = "for any questions or errors contact for number"
    text3 = "number is 7013259413"


    def clear_buttons():
        global doe, doe1

        buttons_to_forget = (l1, l2, l3, l4, doe, doe1)
        for widget in buttons_to_forget:
            if widget is not None:
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
        babble.place(x=100, y=61)

    def gte():
        label.place_forget()
        label1.place_forget()
        label2.place_forget()
        babble.place_forget()

        l1.place(x=243, y=50)
        l2.place(x=100, y=50)
        l3.place(x=100, y=105)
        l4.place(x=100, y=155)
        l5.pack()#GET internet if cmd in__get()

    l5 = Label(root1, image=jarvisimages, width=600, bg="black", relief=RAISED, bd=0)
    l5.pack()

    l1 = Button(root1, image=jbt, bg="#000b1f", height=180, command=aiJ, relief=RAISED, bd=0)
    l1.place(x=243, y=50)

    l2 = Button(root1, text="close", bg="#09f6ff", command=shud, height=3, width=15, relief=RAISED, bd=0)
    l2.place(x=100, y=50)

    l3 = Button(root1, text="Friday", bg="#09f6ff", command=fv, height=3, width=15, relief=RAISED, bd=0)
    l3.place(x=100, y=105)

    l4 = Button(root1, text="More Options", bg="#09f6ff", height=3, width=15, relief=RAISED, bd=0, command=clear_buttons)
    l4.place(x=100, y=155)

    bable = Button(root1, text="instructions", bg="#09f6ff", height=1,command=comd, width=19, relief=RAISED, bd=0)
    bable.place(x=100, y=240)

    root1.mainloop()
except (Exception, ValueError, TypeError) as e:
    # Handle specific exceptions here
    print(e)

