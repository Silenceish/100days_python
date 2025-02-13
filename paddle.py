from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create()        
    
    def create(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=3)        
        self.penup()
        self.seth(90)
    
    def start(self, position):
        self.goto(position)
