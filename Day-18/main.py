from turtle import Screen, Turtle,colormode
import random
tim = Turtle()
tim.color(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions= [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(300):
    tim.color(random_color())
    tim.forward(30)
    tim.right(random.choice(directions))
