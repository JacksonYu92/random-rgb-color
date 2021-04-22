import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours

########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(200):
    degree = [0, 90, 180, 270]
    direction = random.choice(degree) 
    tim.setheading(direction)
    tim.color(random_color())
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(20)