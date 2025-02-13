from turtle import Screen
from paddle import Paddle
import time

PLAYER_START = (-370, 0)
COMP_START = (370, 0)

# Create screen
screen = Screen()
screen.setup(800 , 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player = Paddle()
computer = Paddle()
player.start(PLAYER_START)
computer.start(COMP_START)


game = True

while game:
    
    screen.update()
    time.sleep(0.1)



screen.exitonclick()