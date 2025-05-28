"""
import colorgram

# extract colors from the image
colors = colorgram.extract('image.jpg', 30)

colors_tuples = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    c_t = (r, g, b)
    colors_tuples.append(c_t)

print(colors_tuples)
"""
import turtle
import random


color_list = [(61, 121, 170), (50, 96, 57), (238, 203, 71), (182, 64, 49), (179, 173, 36), (221, 172, 198),
               (182, 51, 56), (211, 87, 57), (46, 46, 95), (209, 163, 187), (133, 160, 186), (38, 39, 80), (37, 84, 45),
               (244, 199, 4), (149, 169, 152), (76, 130, 186), (195, 75, 82), (227, 175, 165), (31, 65, 39),
               (180, 188, 211), (111, 139, 113), (181, 198, 186), (75, 142, 172), (139, 38, 52), (175, 198, 204)]


t = turtle.Turtle()

turtle.colormode(255)
t.hideturtle()
t.speed("fastest")
t.pensize(20)
t.penup()
t.setposition(-200,-200)

for _ in range(10): #largura
    for _ in range(10):
        t.pencolor(random.choice(color_list)) #comprimento
        t.pendown()
        t.forward(1)
        t.penup()
        t.forward(50)
    t.setx(-200)
    t.sety(t.ycor()+50)

screen = turtle.Screen()
screen.exitonclick()