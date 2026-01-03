import turtle
import random

from turtle import Turtle, Screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

color_select = input("Which color do you choose?(red,green,blue,yellow,purple,pink): ")
list_of_colors = ["red", "green", "blue", "yellow", "purple", "pink"]
turtles = []

start_x = -350
start_y = -120
gap = 50
for i in range(6):
    t = turtle.Turtle()
    t.name = f"Turtle{i+1}"
    t.color(list_of_colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(start_x,start_y + i*gap)
    t.write(t.name, align="left", font=("Arial", 20, "bold"))
    t.pendown()
    turtles.append(t)

race_on = True
winner_color =""
while race_on:
    for t in turtles:
        t.forward(random.randint(0, 30))
        if t.xcor() > 230:
            race_on = False
            winner_color = t.pencolor()
            break
turtle.done()

if color_select == winner_color:
    print("You win!")
else:
    print("You lose!")
    print()
print("Thank you for playing!")







