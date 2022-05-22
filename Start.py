# Combine Turtle and Tkinter

import turtle
from tkinter import *

screen = turtle.Screen()
home = screen.getcanvas()

from Animation import T2
T2()
#from Animation import drawA

#drawA(150,150,screen)
home.mainloop()


