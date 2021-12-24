# import all modules
import speech_recognition as sr
import pyttsx3 as pis
import webbrowser as wb
import datetime as dt
import pywhatkit as py
import math
import wikipedia as wi
import pyjokes as pj
from tkinter import *
from tkinter import messagebox
import pygame

lis = sr.Recognizer()
friend = pis.init()

"""RATE"""
rate = friend.getProperty('rate')  # getting details of current speaking rate
friend.setProperty('rate', 150)  # setting up new voice rate


def fv():
    """VOICE"""
    voices = friend.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    friend.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    speak("changed to femail voice sir")


def speak(text):
    friend.say(text)
    friend.runAndWait()


speak("hello this is jarvis the assistant of jeevan")

root = Tk()
root.title("Jarvis")
icon = PhotoImage(file="PIC.png")
root.geometry("600x300")
root.attributes("-alpha", 6.0)
root.iconphoto(False, icon)
root.config(bg="black")  # Happy.root
jarvisimages = PhotoImage(file="jarvis start bt.png")
jbt = PhotoImage(file="Untitled.png")
root.attributes("-alpha", 0.5)


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
                elif "td gaming" in test:
                    speak("opening td gaming sir")
                    url = "https://www.youtube.com/c/TeluguDostGaming"
                    wb.get().open_new(url)
                elif "time" in test:
                    times = dt.datetime.now().strftime("%I:%M %p")
                    Label(root, text=times, fg="#000b1f", bg="black").pack(y=90)
                    speak(times)
                elif "login" in test:
                    login()
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
                elif "google" in test:
                    speak("opening google sir")
                    url = "www.google.com"
                    wb.get().open_new(url)
                elif "cosmic boy" in test:
                    speak("opening the cosmic boy youtube channel sir")
                    url = "https://www.youtube.com/c/TheCosmicBoy1"
                    wb.get().open_new(url)
                elif "cosmic 2" in test:  # HI impoirt  tkinter code=KJIHHJIKewLOPERGJIP@@RIP=instant code of buf gaming app cosmic youtube channel code = wb.Get().new(url).js.py.oot.optb webbroser code = .l::::::olk:::alk
                    speak("opening the cosmic boy 2.0 sir")
                    url = "https://www.youtube.com/c/TheCosmicBoy20"  # the url link of cosmic boy 2.0
                    wb.get().open_new(url)  # cosmic boy 2 gaming youtube channel in the language of telugu
                else:
                    pass


            except:
                pass

    while True:
        command()


def shud():
    messagebox.showinfo("", "do you want to close AI jarvis")
    root.destroy()


Label(root, image=jarvisimages, width=600, bg="black").pack()
Button(root, image=jbt, bg="#000b1f", height=180, command=aiJ).place(x=243, y=50)
Button(root, text="close", bg="#09f6ff", command=shud, height=3, width=15).place(x=100,
                                                                                 y=50) 
Button(root, text="Female voice", bg="#09f6ff", command=fv, height=3, width=15).place(x=100, y=105)


def login():
    root = Tk()
    root.title("Login")
    root.geometry("300x200")
    root.config(background="#000000")
    root.attributes("-alpha", 0.5)

    friend = pis.init()

    def speak(text):
        friend.say(text)
        friend.runAndWait()

    speak("opened Login form")

    def Ok():
        lope = e1.get()
        password = e2.get()
        if (lope == "" and password == ""):
            messagebox.showinfo("", "Login blank is empty")
            speak("Login blank is empty")



        elif (lope == "jeevan" and password == "1"):
            messagebox.showinfo("", "Login done button printed in output")
            Button(root, text="HP open", command=infoolop, height=3, width=13, bg="black", fg="#00ff0d", bd=10,
                   relief=RAISED).place(x=150, y=100)
            speak("Login done button printed in output")

        else:
            messagebox.showinfo("", "Login incorrect")
            speak("Login incorrect")

    global e1
    global e2

    men = "@gmail.com"

    Label(root, text="username", bg="black", fg="#00ff0d").place(x=10, y=10)
    Label(root, text="password", bg="black", fg="#00ff0d").place(x=10, y=40)
    Label(root, bg="black", fg="#00ff0d", height=80).place(x=50, y=180)
    Label(root, text="SIGN", bg="black", fg="#00ff0d", font=("Arial", 100)).place(x=400, y=0)
    Label(root, text="IN", bg="black", fg="#00ff0d", font=("Arial", 100)).place(y=130, x=500)

    e1 = Entry(root)
    e1.place(x=148, y=18)

    e2 = Entry(root)
    e2.place(x=148, y=48)
    e2.config(show="*")

    Button(root, text="Login", command=Ok, height=3, width=13, bg="black", fg="#00ff0d", bd=10, relief=RAISED).place(
        x=10,
        y=100)

    def SH():
        e2.config(show="")

    Radiobutton(root, text="show", bg="black", fg="#00ff0d", command=SH, value=0).place(x=0, y=72)

    def SHO():
        e2.config(show="*")

    Radiobutton(root, text="hide", bg="black", fg="#00ff0d", command=SHO, value=1).place(x=60, y=72)

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New")

    def youtube():
        speak("opening youtube")

        url = "https://www.youtube.com/"
        wb.get().open_new(url)

    def infoolop():
        hack = Tk()
        hack.title('Hp info')
        hack.geometry("1000x1000")
        hack.config(bg="black")
        hack.attributes("-alpha", 0.8)

        speak("opened webbrowser button menu")

        Button(hack, text="youtube", bg="black", fg="#00ff0d", command=youtube, height=3, width=13, bd=10).place(x=0,
                                                                                                                 y=0)
        Button(hack, text="family", bg="black", fg="#00ff0d", command=family, height=3, width=13, bd=10).place(x=0,
                                                                                                               y=70)
        Button(hack, text="chrome", bg="black", fg="#00ff0d", command=bew, height=3, width=13, bd=10).place(x=0, y=150)
        Button(hack, text="whats app", bg="black", fg="#00ff0d", command=whatsapp, height=3, width=13, bd=10).place(x=0,
                                                                                                                    y=220)
        Button(hack, text="snake game", bg="black", fg="yellow", command=snake, height=3, width=13, bd=10).place(x=0,
                                                                                                                 y=290)
        Button(hack, text="counting un", bg="black", fg="#00ff0d", command=counting, height=3, width=13, bd=10).place(
            x=0,
            y=360)
        Button(hack, text="quiz game", bg="black", fg="#00ff0d", command=qgame, height=3, width=13, bd=10).place(x=0,
                                                                                                                 y=430)
        Button(hack, text="password", bg="black", fg="yellow", command=hellopassword, height=3, width=13, bd=10).place(
            x=0,
            y=500)
        Button(hack, text="scratch code", bg="black", fg="#00ff0d", command=scratch, height=3, width=13, bd=10).place(
            x=0,
            y=580)
        Button(hack, text="Google slides", bg="black", fg="#00ff0d", command=slides, height=3, width=13, bd=10).place(
            x=130,
            y=0)
        Button(hack, text="Panzoid", bg="black", fg="#00ff0d", command=pan, height=3, width=13, bd=10).place(x=130,
                                                                                                             y=100)
        Button(hack, text="car game", bg="black", fg="#00ff0d", command=care, height=3, width=13, bd=10).place(x=130,
                                                                                                               y=200)
        Button(hack, text="BMI", bg="black", fg="#00ff0d", command=mio, height=3, width=13, bd=10).place(x=130, y=300)
        Button(hack, text="quiz game", bg="black", fg="#00ff0d", command=lipl, height=3, width=13, bd=10).place(x=130,
                                                                                                                y=400)
        Button(hack, text="music", bg="black", fg="#00ff0d", command=music, height=3, width=13, bd=10).place(x=130,
                                                                                                             y=480)

    def family():
        fm = Tk()
        fm.title("names")
        fm.config(bg="black")

        speak("all family names")

        Label(fm, text="Alekhya", bg="black", fg="#00ff0d").place(x=0, y=0)
        Label(fm, text="vijay", bg="black", fg="#00ff0d").place(x=0, y=30)
        Label(fm, text="ananya", bg="black", fg="#00ff0d").place(x=0, y=50)
        Label(fm, text="innu", bg="black", fg="#00ff0d").place(x=0, y=70)

    def whatsapp():
        speak("opening whats app")

        liuyhks = "https://web.whatsapp.com/"
        wb.get().open_new(liuyhks)

    def bew():
        ulr = "https://www.google.co.in/"
        wb.get().open_new(ulr)

    def snake():
        speak("opening snake game")

        # Creating the Game screen.
        pygame.init()

        white = (255, 255, 255)
        yellow = (255, 255, 102)
        black = (0, 0, 0)
        red = (213, 50, 80)
        green = (0, 255, 0)
        blue = (50, 153, 213)

        dis_width = 600
        dis_height = 400

        # Adding Caption to the screen.
        dis = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game')

        # Enabling Timer.
        clock = pygame.time.Clock()

        # Set spped for snake and Block.
        snake_block = 10
        snake_speed = 9

        # Adding Font style and size.
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("courier", 20, "bold")

        # Setting score
        def Your_score(score):
            value = score_font.render("Made by innu.... Your Score: " + str(score), True, yellow)
            dis.blit(value, [0, 0])

        def our_snake(snake_block, snake_list):
            for x in snake_list:
                pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

        # Meassage Display
        def message(msg, color):
            mesg = font_style.render(msg, True, color)
            dis.blit(mesg, [dis_width / 6, dis_height / 3])

        # Game Loop and Main functions.
        def gameLoop():
            game_over = False
            game_close = False

            x1 = dis_width / 2
            y1 = dis_height / 2

            x1_change = 0
            y1_change = 0

            snake_List = []
            Length_of_snake = 1

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            while not game_over:

                while game_close == True:
                    dis.fill(blue)
                    message("You Lost! Press C-Play Again or Q-Quit", red)
                    Your_score(Length_of_snake - 1)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                game_over = True
                                game_close = False
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x1_change = -snake_block
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT:
                            x1_change = snake_block
                            y1_change = 0
                        elif event.key == pygame.K_UP:
                            y1_change = -snake_block
                            x1_change = 0
                        elif event.key == pygame.K_DOWN:
                            y1_change = snake_block
                            x1_change = 0

                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                    game_close = True
                x1 += x1_change
                y1 += y1_change
                dis.fill(blue)
                pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                snake_Head = []
                snake_Head.append(x1)
                snake_Head.append(y1)
                snake_List.append(snake_Head)
                if len(snake_List) > Length_of_snake:
                    del snake_List[0]

                for x in snake_List[:-1]:
                    if x == snake_Head:
                        game_close = True

                our_snake(snake_block, snake_List)
                Your_score(Length_of_snake - 1)

                pygame.display.update()

                if x1 == foodx and y1 == foody:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    Length_of_snake += 1

                clock.tick(snake_speed)

            pygame.quit()
            quit()

        gameLoop()

    def counting():
        speak("count until unlemited")

        n = int(input("enter n value:"))
        i = 1  # loop variabale
        while i <= n:
            print(i, end="")
            i = i + 1

    def qgame():
        speak("welcome to the quiz game")

        answer = "innu"
        qustion = input("who made this quiz game tell his name:")

        if answer == qustion:
            print("correct answer go to the next qustion")

        else:
            print("incorrect answer go to the next qustions")

        answerone = "python"
        qustionone = input("with which programing language does this quiz game made:")

        if answerone == qustionone:
            print("correct answer go to the next qustion")

        else:
            print("incorrect answer go to the next qustions")

        passwordtwo = "6"
        enpasswordtwo = input("2.5 + 3.5 = :")
        if passwordtwo == enpasswordtwo:
            print("correct answer")

        else:
            print("wrong password you cant play quiz game try next time")

            print("you finished the quiz game")

    def hellopassword():
        speak("opening password screen")

        hack = Tk()
        hack.title("Enter the password")
        hack.geometry("300x200")
        hack.config(background="black")

        def rot():
            lab = r1.get()
            if (lab == "123"):
                messagebox.showinfo("", "password is correct")




            elif (lab == ""):
                messagebox.showinfo("", "blank is empty")

            else:
                messagebox.showinfo("", "password incorrect")

        global r1

        Label(hack, text="pleas enter the password:", bg="black", fg="#ffffff").place(x=0, y=0)

        r1 = Entry(hack)
        r1.place(x=138, y=1)
        r1.config(show="*")
        r1.bg = "red"

        Button(hack, text="enter", command=rot, bg="#ffffff").place(x=220, y=25)

        def ROU():
            r1.config(show="")

        Radiobutton(hack, text="show", command=ROU, value=1, bg="black", fg="yellow").place(x=0, y=22)

        def ROP():
            r1.config(show="*")

        Radiobutton(hack, text="hide", command=ROP, value=2, bg="black", fg="yellow").place(x=0, y=50)

        def ROPE():
            r1.config(show="⚫")

        Radiobutton(hack, text="show as ⚫", command=ROPE, value=3, bg="black", fg="yellow").place(x=55, y=23)

        def ROPES():
            r1.config(show="$")

        Radiobutton(hack, text="show as $", command=ROPES, value=4, bg="black", fg="yellow").place(x=55, y=50)

        def ROPEO():
            r1.config(show="@")

        Radiobutton(hack, text="show as @", command=ROPEO, value=5, bg="black", fg="yellow").place(x=55, y=80)

    def scratch():
        speak("opening scratch programing")

        link = "https://scratch.mit.edu/"
        wb.get().open_new(link)

    def slides():
        speak("opening google slides")

        linkone = "https://docs.google.com/presentation/u/0/"
        wb.get().open_new(linkone)

    def pan():
        speak("opening panzoid")

        wbl = "https://panzoid.com/"
        wb.get().open_new(wbl)

    def care():
        speak("opening car game")

        # RGB
        gray = (119, 118, 110)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 200, 0)
        blue = (0, 0, 200)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)
        bright_blue = (0, 0, 255)
        display_width = 800
        display_height = 600

        # display setup
        gamedisplays = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("car game")
        clock = pygame.time.Clock()
        carimg = pygame.image.load('car1.jpg')
        backgroundpic = pygame.image.load("download12.jpg")
        yellow_strip = pygame.image.load("yellow strip.jpg")
        intro_background = pygame.image.load("0.jpg")
        strip = pygame.image.load("strip.jpg")

        instruction_background = pygame.image.load("2.jpg")
        car_width = 56
        pause = False

        # for game intro statments
        def intro_loop():
            intro = True
            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
                gamedisplays.blit(intro_background, (0, 0))
                largetext = pygame.font.Font(None, 115)
                TextSurf, TextRect = text_objects("car game", largetext)
                TextRect.center = (400, 100)
                gamedisplays.blit(TextSurf, TextRect)
                button("START", 150, 520, 100, 50, green, bright_green, "play")
                button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")

                pygame.display.update()
                clock.tick(50)

        # buttons and mouse events
        def button(msg, x, y, w, h, ic, ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
                if click[0] == 1 and action != None:
                    if action == "play":
                        countdown()
                    elif action == "quit": #js.inter.fast
                        pygame.quit()
                        quit()
                        sys.exit()
                    elif action == "intro":
                        introduction()
                    elif action == "menu":
                        intro_loop()
                    elif action == "pause":
                        paused()
                    elif action == "unpause":
                        unpaused()


            else:
                pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
            smalltext = pygame.font.Font("freestanding.ttf", 20)
            textsurf, textrect = text_objects(msg, smalltext)
            textrect.center = ((x + (w / 2)), (y + (h / 2)))
            gamedisplays.blit(textsurf, textrect)

        def introduction():
            introduction = True
            while introduction:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
                gamedisplays.blit(instruction_background, (0, 0))
                largetext = pygame.font.Font('freesansbold.ttf', 80)
                smalltext = pygame.font.Font('freesansbold.ttf', 20)
                mediumtext = pygame.font.Font('freesansbold.ttf', 40)
                textSurf, textRect = text_objects("This is an car game in which you need dodge the coming cars",
                                                  smalltext)
                textRect.center = ((350), (200))
                TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
                TextRect.center = ((400), (100))
                gamedisplays.blit(TextSurf, TextRect)
                gamedisplays.blit(textSurf, textRect)
                stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", smalltext)
                stextRect.center = ((150), (400))
                hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
                hTextRect.center = ((150), (450))
                atextSurf, atextRect = text_objects("A : ACCELERATOR", smalltext)
                atextRect.center = ((150), (500))
                rtextSurf, rtextRect = text_objects("B : BRAKE ", smalltext)
                rtextRect.center = ((150), (550))
                ptextSurf, ptextRect = text_objects("P : PAUSE  ", smalltext)
                ptextRect.center = ((150), (350))
                sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
                sTextRect.center = ((350), (300))
                gamedisplays.blit(sTextSurf, sTextRect)
                gamedisplays.blit(stextSurf, stextRect)
                gamedisplays.blit(hTextSurf, hTextRect)
                gamedisplays.blit(atextSurf, atextRect)
                gamedisplays.blit(rtextSurf, rtextRect)
                gamedisplays.blit(ptextSurf, ptextRect)
                button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")
                pygame.display.update()
                clock.tick(30)

        def paused():
            global pause

            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
                gamedisplays.blit(instruction_background, (0, 0))
                largetext = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("PAUSED", largetext)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(TextSurf, TextRect)
                button("CONTINUE", 150, 450, 150, 50, green, bright_green, "unpause")
                button("RESTART", 350, 450, 150, 50, blue, bright_blue, "play")
                button("MAIN MENU", 550, 450, 200, 50, red, bright_red, "menu")
                pygame.display.update()
                clock.tick(30)

        def unpaused():
            global pause
            pause = False

        def countdown_background():
            font = pygame.font.SysFont(None, 25)
            x = (display_width * 0.45)
            y = (display_height * 0.8)
            gamedisplays.blit(backgroundpic, (0, 0))
            gamedisplays.blit(backgroundpic, (0, 200))
            gamedisplays.blit(backgroundpic, (0, 400))
            gamedisplays.blit(backgroundpic, (700, 0))
            gamedisplays.blit(backgroundpic, (700, 200))
            gamedisplays.blit(backgroundpic, (700, 400))
            gamedisplays.blit(yellow_strip, (400, 100))
            gamedisplays.blit(yellow_strip, (400, 200))
            gamedisplays.blit(yellow_strip, (400, 300))
            gamedisplays.blit(yellow_strip, (400, 400))
            gamedisplays.blit(yellow_strip, (400, 100))
            gamedisplays.blit(yellow_strip, (400, 500))
            gamedisplays.blit(yellow_strip, (400, 0))
            gamedisplays.blit(yellow_strip, (400, 600))
            gamedisplays.blit(strip, (120, 200))
            gamedisplays.blit(strip, (120, 0))
            gamedisplays.blit(strip, (120, 100))
            gamedisplays.blit(strip, (680, 100))
            gamedisplays.blit(strip, (680, 0))
            gamedisplays.blit(strip, (680, 200))
            gamedisplays.blit(carimg, (x, y))
            text = font.render("level: 0", True, bright_green)
            score = font.render("SCORE: 0", True, blue)
            gamedisplays.blit(text, (0, 50))
            gamedisplays.blit(score, (0, 30))
            button("PAUSE", 650, 0, 150, 50, black, "pause")

        def countdown():
            countdown = True

            while countdown:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        sys.exit()
                gamedisplays.fill(gray)
                countdown_background()
                largetext = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("3", largetext)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(TextSurf, TextRect)
                pygame.display.update()
                clock.tick(1)
                gamedisplays.fill(gray)
                countdown_background()
                largetext = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("2", largetext)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(TextSurf, TextRect)
                pygame.display.update()
                clock.tick(1)
                gamedisplays.fill(gray)
                countdown_background()
                largetext = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("1", largetext)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(TextSurf, TextRect)
                pygame.display.update()
                clock.tick(1)
                gamedisplays.fill(gray)
                countdown_background()
                largetext = pygame.font.Font('freesansbold.ttf', 115)
                TextSurf, TextRect = text_objects("--GO--", largetext)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(TextSurf, TextRect)
                pygame.display.update()
                clock.tick(1)
                game_loop()

        def obstacle(obs_startx, obs_starty, obs):
            if obs == 0:
                obs_pic = pygame.image.load("car.jpg")
            elif obs == 1:
                obs_pic = pygame.image.load("car1.jpg")
            elif obs == 2:
                obs_pic = pygame.image.load("car2.jpg")
            elif obs == 3:
                obs_pic = pygame.image.load("car4.jpg")
            elif obs == 4:
                obs_pic = pygame.image.load("car5.jpg")
            elif obs == 5:
                obs_pic = pygame.image.load("car6.jpg")
            elif obs == 6:
                obs_pic = pygame.image.load("car7.jpg")
            gamedisplays.blit(obs_pic, (obs_startx, obs_starty))

        def score_system(passed, score):
            font = pygame.font.SysFont(None, 25)
            text = font.render("Passed" + str(passed), True, black)
            score = font.render("Score" + str(score), True, red)
            gamedisplays.blit(text, (0, 50))
            gamedisplays.blit(score, (0, 30))

        def text_objects(text, font):
            textsurface = font.render(text, True, bright_blue)
            return textsurface, textsurface.get_rect()

        def message_display(text):
            largetext = pygame.font.Font("freesansbold.ttf", 30)
            textsurf, textrect = text_objects(text, largetext)
            textrect.center = ((display_width / 2), (display_height / 2))
            gamedisplays.blit(textsurf, textrect)
            pygame.display.update()
            time.sleep(3)
            game_loop()

        def crash():
            message_display("CRASHED")

        def background():
            gamedisplays.blit(backgroundpic, (0, 0))
            gamedisplays.blit(backgroundpic, (0, 200))
            gamedisplays.blit(backgroundpic, (0, 400))
            gamedisplays.blit(backgroundpic, (700, 0))
            gamedisplays.blit(backgroundpic, (700, 200))
            gamedisplays.blit(backgroundpic, (700, 400))
            gamedisplays.blit(yellow_strip, (400, 0))
            gamedisplays.blit(yellow_strip, (400, 100))
            gamedisplays.blit(yellow_strip, (400, 200))
            gamedisplays.blit(yellow_strip, (400, 300))
            gamedisplays.blit(yellow_strip, (400, 400))
            gamedisplays.blit(yellow_strip, (400, 500))
            gamedisplays.blit(strip, (120, 0))
            gamedisplays.blit(strip, (120, 100))
            gamedisplays.blit(strip, (120, 200))
            gamedisplays.blit(strip, (680, 0))
            gamedisplays.blit(strip, (680, 100))
            gamedisplays.blit(strip, (680, 200))

        def car(x, y):
            gamedisplays.blit(carimg, (x, y))

        def game_loop():
            global pause
            x = (display_width * 0.45)
            y = (display_height * 0.8)
            x_change = 0
            obstacle_speed = 9
            obs = 0
            y_change = 0
            obs_startx = random.randrange(200, (display_width - 200))
            obs_starty = -750
            obs_width = 56
            obs_height = 125
            passed = 0
            level = 0
            score = 0
            y2 = 7
            fps = 120

            bumped = False
            while not bumped:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        if event.key == pygame.K_RIGHT:
                            x_change = 5
                        if event.key == pygame.K_a:
                            obstacle_speed += 2
                        if event.key == pygame.K_b:
                            obstacle_speed -= 2
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x_change = 0

                x += x_change
                pause = True
                gamedisplays.fill(gray)

                rel_y = y2 % backgroundpic.get_rect().width
                gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
                gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
                if rel_y < 800:
                    gamedisplays.blit(backgroundpic, (0, rel_y))
                    gamedisplays.blit(backgroundpic, (700, rel_y))
                    gamedisplays.blit(yellow_strip, (400, rel_y))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 100))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 200))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 300))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 400))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 500))
                    gamedisplays.blit(yellow_strip, (400, rel_y - 100))
                    gamedisplays.blit(strip, (120, rel_y - 200))
                    gamedisplays.blit(strip, (120, rel_y + 20))
                    gamedisplays.blit(strip, (120, rel_y + 30))
                    gamedisplays.blit(strip, (680, rel_y - 100))
                    gamedisplays.blit(strip, (680, rel_y + 20))
                    gamedisplays.blit(strip, (680, rel_y + 30))

                y2 += obstacle_speed

                obs_starty -= (obstacle_speed / 4)
                obstacle(obs_startx, obs_starty, obs)
                obs_starty += obstacle_speed
                car(x, y)
                score_system(passed, score)
                if x > 690 - car_width or x < 110:
                    crash()
                if x > display_width - (car_width + 110) or x < 110:
                    crash()
                if obs_starty > display_height:
                    obs_starty = 0 - obs_height
                    obs_startx = random.randrange(170, (display_width - 170))
                    obs = random.randrange(0, 7)
                    passed = passed + 1
                    score = passed * 10
                    if int(passed) % 10 == 0:
                        level = level + 1
                        obstacle_speed + 2
                        largetext = pygame.font.Font("freesansbold.ttf", 80)
                        textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                        textrect.center = ((display_width / 2), (display_height / 2))
                        gamedisplays.blit(textsurf, textrect)
                        pygame.display.update()
                        time.sleep(3)

                if y < obs_starty + obs_height:
                    if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                        crash()
                button("Pause", 650, 0, 150, 50, blue, bright_blue, "pause")
                pygame.display.update()
                clock.tick(60)

        intro_loop()
        game_loop()
        pygame.quit()
        quit()

    def mio():
        speak("opening BMI calculator")

        print("BMI CALCULATOR")
        print("BMI CALCULATOR by innu")

        x = float(input("enter your height in meters."))
        y = float(input("enter your weight kilograms."))

        BMI = y / (x ** 2)
        print("BMI:")
        print("BMI")
        print("thank you for using our BMI Calculator")
        if BMI <= 18.50:
            print("Underweight eat little more friend..!")
            print("All the best")
        if BMI > 18.50 and BMI < 24.99:
            print("Normal.good JOB, your fit")
            print("maintain this")

        if BMI > 25.0 and BMI < 29.99:
            print("OverWeight ..!")
            print("take care ..practice a diet")
        elif BMI > 30:
            print("you are OBESE ..! maintain DIET")

    def lipl():
        root = Tk()
        root.title("Tutorial")
        root.geometry("900x600")
        root.config(background="#000000")

        def q1():

            au1 = u1.get()
            if (au1 == "innu"):
                messagebox.showinfo("", "correct answer")

            elif (au1 == ""):
                messagebox.showinfo("", "answer blank is empty")

            else:
                messagebox.showinfo("", "incorrect answer")

        u1 = Entry(root)
        u1.place(x=70, y=0)
        u1.config(show="*")

        Button(root, text="enter", command=q1, bg="black", fg="#00ff0d", height=3, width=13, bd=10,
               relief=RAISED).place(
            x=70, y=20)

        def so():
            u1.config(show="")

        Radiobutton(root, text="show", bg="black", fg="#00ff0d", command=so, value=0).place(x=0, y=20)

        def ho():
            u1.config(show="*")

        Radiobutton(root, text="hide", bg="black", fg="#00ff0d", command=ho, value=0).place(x=0, y=40)

        Label(root, text="game by:", bg="black", fg="#00ff0d").place(x=0, y=0)

    def htg():
        speak("playing harry potter music")

        pygame.mixer.music.load("Believer_192(PagalWorld).mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.70)

    def htgs():
        pygame.mixer.music.stop()

    def music():
        mus = Tk()
        mus.title("play music")
        mus.config(bg="black")
        mus.geometry("500x400")

        Button(mus, text="play", bg="black", fg="#00ff0d", command=htg, font=("Helvetica", 32), bd=10).pack(pady=20)
        Button(mus, text="stop", bg="black", fg="#00ff0d", command=htgs, bd=10).pack(pady=20)

    root.mainloop()


root.mainloop()
