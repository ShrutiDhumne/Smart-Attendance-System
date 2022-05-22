# Swastik Method

import turtle
import tkinter.ttk as ttk
from tkinter.ttk import Progressbar
Screen = ''
def T() : 
    """mario = turtle.Turtle(shape = 'classic')
    mario.speed('fast')
    mario.penup()
    mario.setpos(-10,-50)
    mario.bk(20)
    p = mario.position()
    mario.setpos((p[0]-5,p[1]-20))
    mario.pendown()
    mario.speed('fast') #slow
    mario.color('white')
    mario.rt(90)
    mario.fd(50)
    mario.lt(90)
    mario.fd(100)
    mario.rt(90)
    mario.fd(50)
    mario.penup()
    mario.rt(90)
    mario.fd(100)
    P = mario.position()
    mario.pendown()
    mario.bk(50)
    mario.rt(90)
    mario.fd(100)
    mario.rt(90)
    mario.fd(50)
    mario.ht()
    mario.penup()
    mario.st()
    mario.setx(P[0]+50)
    mario.sety(P[1]-50)
    mario.pendown()
    mario.circle(100)
    mario.ht()"""
    global Screen
    turtle.ht()
    turtle.delay(20)
    turtle.hideturtle()
    import Project as P
    Screen.bye()
    P.start()
    turtle.done()

def T2(screen) :
    global Screen
    Screen = screen
    
    turtle.penup()
    #t = turtle.Turtle();   t.setx(150);   #t.sety(400)
    turtle.bgpic('Dataset/welcome.png')
    turtle.color('yellow')
    
    turtle.setpos(-50,30)
    style = ('milkshake', 20, 'bold')
    turtle.write('Welcome to \n', font=style, align='right')
    turtle.setpos(50,0)
    turtle.write('\n\n\n Smart Attendance System', font=style, align='right')
    turtle.setpos(00, -200)
    turtle.color('red')
    style = ('milkshake', 10, 'bold')
    turtle.write('Press Enter to continue!', font=style, align='right')
    screen.onkey(T,'Return')
    turtle.ht()
    screen.listen()
    turtle.done()








def drawA(width, height):
    """
    someOlTurtle will draw the letter A with a given width and height,
    with the current location being the lower left corner of the A.
    """
    #someOlTurtle = turtle.Turtle()
    # figure out where we are
    someOlTurtle = turtle.Turtle()
    startX = someOlTurtle.xcor()
    startY = someOlTurtle.ycor()

    # figure out the other points using only what we know,
    # which is width, height, startX and startY
    
    topAX = startX + (width/2)
    topAY = startY + height

    bottomRightX = startX + width
    bottomRightY = startY
    
    barLeftX = startX + width/4
    barLeftY = startY + height/2

    barRightX = startX + (width/4) + (width/2)
    barRightY = startY + height/2
    
    # draw left hand side of the A    
    someOlTurtle.goto(topAX,topAY)

    # draw the right side of the A

    someOlTurtle.goto(bottomRightX, bottomRightY)

    # draw bar across the middle
    
    someOlTurtle.up()
    someOlTurtle.goto(barLeftX,barLeftY)
    someOlTurtle.down()
    someOlTurtle.goto(barRightX,barRightY)

    # leave turtle at lower right hand corner of letter
    
    someOlTurtle.up()
    someOlTurtle.goto(bottomRightX,bottomRightY)
    someOlTurtle.down()