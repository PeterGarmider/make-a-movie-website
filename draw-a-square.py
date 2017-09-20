import turtle

window = turtle.Screen()
window.bgcolor("red")
def draw_square():

    vehicle = turtle.Turtle()
    vehicle.shape("turtle")
    vehicle.color("blue")
    vehicle.speed(10)

    counter = 0
    while counter < 100:
        vehicle.forward(100)
        vehicle.right(90)
        counter = counter+1

def draw_circle():
    boat = turtle.Turtle()
    boat.shape("circle")
    boat.color("green")
    boat.speed(100)

    counter = 0
    while counter < 100:
        boat.circle(100)
        boat.forward(10)
        boat.right(90)
        boat.forward(30)
        boat.circle(100)
        counter = counter+1

def draw_triangle():
    plane = turtle.Turtle()
    plane.shape("triangle")
    plane.color("purple")
    plane.speed(10)

    counter = 0
    while counter < 100:
        plane.forward(200)
        plane.right(120)
        plane.forward(200)
        plane.right(60)
        plane.forward(200)
        plane.right(120)
        counter = counter+1

    window.exitonclick()
draw_square()
draw_circle()
draw_triangle()