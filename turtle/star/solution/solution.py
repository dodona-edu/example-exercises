import turtle

n = int(input())

turtle.color("orange")
turtle.pensize(3)
for _ in range(n):
    turtle.forward(150)
    turtle.right(180 - 180 / n)
