import turtle

n = int(input())

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

segment_radius = 20
segment_spacing = 35

# Draw body segments from back to front
for i in range(n - 1, -1, -1):
    x = -((n - 1) * segment_spacing) / 2 + i * segment_spacing
    t.penup()
    t.goto(x, -segment_radius)
    t.pendown()
    t.pensize(2)
    t.pencolor("darkgreen")
    t.fillcolor("limegreen")
    t.begin_fill()
    t.circle(segment_radius)
    t.end_fill()

# Head is the first segment (leftmost)
head_x = -((n - 1) * segment_spacing) / 2

# Eyes
for dx in (-8, 8):
    t.penup()
    t.goto(head_x + dx, 5)
    t.pendown()
    t.pencolor("black")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(6)
    t.end_fill()

    # Pupil
    t.penup()
    t.goto(head_x + dx + 2, 7)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

# Smile
t.penup()
t.goto(head_x + 8, -5)
t.setheading(270)
t.pendown()
t.pensize(2)
t.pencolor("black")
t.circle(-8, 180)

# Antennae
for dx, angle in ((-6, 130), (6, 50)):
    t.penup()
    t.goto(head_x + dx, segment_radius)
    t.setheading(angle)
    t.pendown()
    t.pensize(2)
    t.pencolor("darkgreen")
    t.forward(25)
    # Small ball at the tip
    t.fillcolor("red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

turtle.done()
