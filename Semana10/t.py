import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
t = turtle.Turtle()
t.speed(10)

# Draw the base of the house
t.penup()
t.goto(-50, -50)
t.pendown()
t.fillcolor("burlywood")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Draw the roof
t.fillcolor("firebrick")
t.begin_fill()
t.left(45)
t.forward(70)
t.right(90)
t.forward(70)
t.right(135)
t.forward(100)
t.end_fill()

# Draw the door
t.penup()
t.goto(-15, -50)
t.pendown()
t.fillcolor("saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

# Draw a window
t.penup()
t.goto(20, 0)
t.pendown()
t.fillcolor("lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()