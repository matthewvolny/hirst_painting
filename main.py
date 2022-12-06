from turtle import Turtle, Screen, colormode
import random

pointer = Turtle()
colormode(255)

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

#random walk with random color
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     tuple = (r,g,b)
#     return tuple

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
#     pointer.color(random_color())
#     turn_random_direction()
#     pointer.forward(40)
    
#spirograph
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple = (r,g,b)
    return tuple


for i in range (50):
    pointer.speed("fastest")
    pointer.pd()
    pointer.color(random_color())
    pointer.circle(100)
    pointer.left(7.2)



screen = Screen()
screen.exitonclick()