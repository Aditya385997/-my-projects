import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pygame
import pyjokes
import sys
import random
import os
import turtle as t


pygame.init()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'noob' in command:
                command = command.replace('noob', '')
                print(command)
    except:
        pass
    return command


def run_noob():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'move' in command:
        talk('the car is moving')
        car_start_without_obstacle()
    elif 'stop' in command:
        talk('stopping the car')
        car_avoid_obstacle()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%m %p')
        print(time)
        talk('current time is ' + time)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i have a boyfriend')
    elif 'are you single' in command:
        talk('srry got a relation with the wifi')
    elif 'bye' in command:
        talk('have a great day')
        return False
    elif 'how are you' in command:
        talk('im good')
    elif 'create text file' in command:
        talk('please wait creating the file')
        text_file()
    elif 'create html file' in command:
        talk('please wait creating the file')
        html_file()
    elif 'create css file' in command:
        talk('please wait creating the file')
        css_file()
    elif 'create python file' in command:
        talk('please wait creating the file')
        python_file()
    elif 'start pong game' in command:
        talk('starting the pong game')
        block_game()
    elif 'create a folder' in command:
        talk('creating the folder')
        create_folder()
    elif 'text' in command:
        talk("your request is proceeding")
        whats_app()
    else:
        talk("please say command again")
    return True


def car_start_without_obstacle():
    window = pygame.display.set_mode((1200, 400))
    track = pygame.image.load('track1.png')
    car = pygame.image.load('tesla.png')
    car = pygame.transform.scale(car, (30, 60))
    car_x = 150
    car_y = 300
    focal_dis = 25
    clock = pygame.time.Clock()
    while (True):
        clock.tick(60)
        cam_x = car_x + 15
        cam_y = car_y + 15
        up_px = window.get_at((cam_x, cam_y-focal_dis))[0]
        # print(up_px)
        if up_px == 255:
            car_y = car_y - 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 0, 255), (cam_x, cam_y), 5, 5)
        pygame.display.update()


def car_avoid_obstacle():
    window = pygame.display.set_mode((1200, 400))
    track = pygame.image.load('track2.png')
    car = pygame.image.load('tesla.png')
    car = pygame.transform.scale(car, (30, 60))
    car_x = 150
    car_y = 300
    focal_dis = 25
    clock = pygame.time.Clock()
    while (True):
        clock.tick(60)
        cam_x = car_x + 15
        cam_y = car_y + 15
        up_px = window.get_at((cam_x, cam_y-focal_dis))[0]
        # print(up_px)
        if up_px == 255:
            car_y = car_y - 2
        window.blit(track, (0, 0))
        window.blit(car, (car_x, car_y))
        pygame.draw.circle(window, (0, 0, 255), (cam_x, cam_y), 5, 5)
        pygame.display.update()


def text_file():
    file = open("C:\\Users\\91704\\Desktop\\work\\files\\new.txt", 'w')
    talk('your file have been created Happy hacking!!!')


def html_file():
    file = open("C:\\Users\\91704\\Desktop\\work\\files\\new.html", 'w')
    talk("your file have been created happy hacking")


def css_file():
    file = open("C:\\Users\\91704\\Desktop\\work\\files\\new.css", 'w')
    talk("your file have been created happy hacking")


def python_file():
    file = open("C:\\Users\\91704\\Desktop\\work\\files\\new.py", 'w')
    talk("your file have been created happy hacking")


def create_folder():
    path = "C:\\Users\\91704\\Desktop\\work\\files"
    os.chdir(path)
    talk('what you wanna keep the name of the folder')
    command = take_command()
    newfolder = (command)
    os.makedirs(newfolder)
    talk("your folder have been created happy hacking")


def block_game():
    playerAscore = 0
    playerBscore = 0
    window = t.Screen()
    window.title("pong game")
    window.bgcolor("green")
    window.setup(width=800, height=600)
    window.tracer(0)

    leftpaddle = t.Turtle()
    leftpaddle.speed(0)
    leftpaddle.shape('square')
    leftpaddle.color('white')
    leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
    leftpaddle.penup()
    leftpaddle.goto(-350, 0)

    rightpaddle = t.Turtle()
    rightpaddle.speed(0)
    rightpaddle.shape('square')
    rightpaddle.color('white')
    rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightpaddle.penup()
    rightpaddle.goto(350, 0)

    ball = t.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color('red')
    ball.penup()
    ball.goto(5, 5)
    ballxdirection = 0.2
    ballydirection = 0.2

    pen = t.Turtle()
    pen.speed(0)
    pen.color('blue')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write('score', align='center', font=('Arial', 24, 'normal'))

    def leftpaddle_up():
        y = leftpaddle.ycor()
        y = y+90
        leftpaddle.sety(y)

    def leftpaddle_down():
        y = leftpaddle.ycor()
        y = y-90
        leftpaddle.sety(y)

    def rightpaddle_up():
        y = rightpaddle.ycor()
        y = y+90
        rightpaddle.sety(y)

    def rightpaddle_down():
        y = rightpaddle.ycor()
        y = y-90
        rightpaddle.sety(y)

    window.listen()
    window.onkeypress(leftpaddle_up, "w")
    window.onkeypress(leftpaddle_down, "s")
    window.onkeypress(rightpaddle_up, "Up")
    window.onkeypress(rightpaddle_down, "Down")

    while(True):
        window.update()

        ball.setx(ball.xcor() + ballxdirection)
        ball.sety(ball.ycor() + ballydirection)

        if ball.ycor() > 290:
            ball.sety(290)
            ballydirection = ballydirection * -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ballydirection = ballydirection * -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ballxdirection = ballxdirection * -1
            playerAscore = playerAscore + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(
                playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")
        if(ball.xcor()) < -390:
            ball.goto(0, 0)
            ballxdirection = ballxdirection * -1
            playerBscore = playerBscore + 1
            pen.clear()
            pen.write("Player A: {}                    Player B: {} ".format(
                playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
            os.system("afplay wallhit.wav&")
        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
            ball.setx(340)
            ballxdirection = ballxdirection * -1
            os.system("afplay paddle.wav&")

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
            ball.setx(-340)
            ballxdirection = ballxdirection * -1
            os.system("afplay paddle.wav&")


def whats_app():
    talk("what text u wanna type")
    command = take_command()
    
    pywhatkit.sendwhatmsg("+917447290136", command)

while(True):
    continue_noob = run_noob()
    if not continue_noob:
        break
