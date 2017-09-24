
import turtle
import math

window = turtle.Screen()
window.bgcolor("yellow")

"""def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
"""
def draw_square():

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("blue")
    bob.speed(10)

    rotation_counter = 0
    while rotation_counter < 36:
        bob.right(10)
        rotation_counter = rotation_counter + 1

        square_counter = 0
        while square_counter < 4:
            bob.forward(100)
            bob.right(90)
            square_counter = square_counter+1

"""
def draw_circle():
    boat = turtle.Turtle()
    boat.shape("circle")
    boat.color("green")
    boat.speed(100)

    counter = 0
    while counter < 10:
        boat.circle(100)
        counter = counter+1
"""


def draw_triangle():
    mike = turtle.Turtle()
    mike.color("purple")
    mike.speed(100)

    rotation_counter = 0
    while rotation_counter < 300:
        mike.right(45)
        mike.forward(20 + rotation_counter)
        rotation_counter = rotation_counter + 1

        triangle_counter = 0
        while triangle_counter < 4:
            mike.right(55)
            mike.forward(math.exp(triangle_counter+1))
            triangle_counter = triangle_counter + 1

    window.exitonclick()

draw_triangle()
#draw_square()