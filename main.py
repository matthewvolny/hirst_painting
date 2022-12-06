from turtle import Turtle, Screen
import random

import heroes
print(heroes.gen())
# class Pointer:
#     def __init__(self, name):
#         self.name = name
#         pointer = Turtle(name)

# pointer = Pointer("John")

pointer = Turtle()

# draw a box
# for i in range (0,4):
#     pointer.forward(100)
#     pointer.left(90)

# draw a dotted line
# for i in range (0, 5):
#     pointer.pd()
#     pointer.forward(30)
#     pointer.pu()
#     pointer.forward(30)

#draw nested shapes
# def draw_shape(sides, angle, color):
#     pointer.color(color)
#     for i in range(sides):
#         pointer.pd()
#         pointer.forward(100)
#         pointer.right(angle)

# draw_shape(3, 120, "red") # triangle
# draw_shape(4, 90, "green") # square
# draw_shape(5, 72, "orange") # pentagon
# draw_shape(6, 60, "teal") # hexagon
# draw_shape(7, 51.43, "purple") # heptagon
# draw_shape(8, 45, "blue") # octagon
# draw_shape(9, 40, "pink") # nonagon
# draw_shape(10, 36, "gray") # decagon

#random walk
# color_palette = ['light salmon', 'violet', 'pale green', 'light sky blue', 'bisque']
# directions = ['left', 'right', 'forward', 'back']

# def turn_random_direction():
#     random_direction = random.choice(directions)
#     if random_direction == 'left':
#         pointer.left(90)
#     elif random_direction == 'right':
#         pointer.right(90)
#     elif random_direction == 'back':
#         pointer.right(180)    

# for i in range (100):
#     pointer.pd()
#     pointer.pensize(20)
#     pointer.speed(10)
#     pointer.color(random.choice(color_palette))
#     turn_random_direction()
#     pointer.forward(40)

    

screen = Screen()
screen.exitonclick()