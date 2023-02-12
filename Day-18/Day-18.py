from turtle import Screen, Turtle
import random
colors = ["cornflower blue","medium spring green","red","violet","medium purple","yellow","orange"]

tim = Turtle()

#for _ in range(100):

tim.circle(100)
tim.speed("fastest")

#for _ in range(100):
    #tim.color(random.choice(colors))
    #tim.setheading(tim.heading() + 10)
    #im.circle(100)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(5)

screen = Screen()
screen.exitonclick() 