import tkinter as tk
import tkinter.font as tkFont
import turtle

class App :
    def __init__(self, root) :
        import Welcome as welcome
        welcome.main(root)
    
def start() :
    #f __name__ == "__main__":
    root = tk.Tk()
    app = App(root)   
    root.mainloop()

if __name__ == '__main__' :
  
    import turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    home = screen.getcanvas()
    from Animation import T2
    T2(screen)
    #start()
    home.mainloop()
    