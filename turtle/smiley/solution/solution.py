import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Smiley Face!")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def filled_circle(x, y, radius, fill_color, pen_color="black", pen_width=2):
    """Draw a filled circle with its center at (x, y)."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pensize(pen_width)
    t.pencolor(pen_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# Face
filled_circle(0, 0, 110, "gold")

# Eyes (white sclera)
filled_circle(-40, 35, 18, "white")
filled_circle(40, 35, 18, "white")

# Pupils
filled_circle(-38, 28, 9, "black", "black")
filled_circle(38, 28, 9, "black", "black")

# Eyebrows
t.penup()
t.pensize(5)
t.pencolor("saddlebrown")
t.goto(-57, 62)
t.pendown()
t.goto(-23, 68)

t.penup()
t.goto(23, 68)
t.pendown()
t.goto(57, 62)

# Nose
filled_circle(0, -5, 8, "tomato", "tomato")

# Rosy cheeks
filled_circle(-83, -8, 20, "lightpink", "lightpink")
filled_circle(83, -8, 20, "lightpink", "lightpink")

# Smile: arc from (60, -30) clockwise through (0, -90) to (-60, -30)
t.penup()
t.pensize(5)
t.pencolor("black")
t.goto(60, -30)
t.setheading(270)
t.pendown()
t.circle(-60, 180)

turtle.done()
