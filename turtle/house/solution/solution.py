import turtle


def house():
    # Draw a blue house
    turtle.color("blue")

    # Draw the base/square
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)

    # Move up
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()

    # Draw the roof/triangle
    turtle.right(30)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)


house()
