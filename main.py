import turtle
import random
from turtle import*
t = turtle.Turtle()

colors=['red', 'green', 'blue', 'orange']

for i in range(100):
   color(random.choice(colors))
   forward(i)
   right(36)
print(5)
