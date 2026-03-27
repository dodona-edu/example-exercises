In this exercise, you'll use the `turtle` module to draw a **caterpillar**.

Your program should:

1. Read an **integer** from input: the number of body segments.
2. Draw a caterpillar with exactly that many segments.

Your caterpillar should have at least:
- The correct number of **body segments** (circles work great!)
- A **face** on the head segment (eyes and a mouth)
- Two **antennae**

Feel free to get creative! You could add:
- Colorful segments — alternate colors or use a gradient
- Tiny legs underneath each segment
- A fun background like grass or flowers
- Spots or patterns on the body

Here's one possible outcome with 6 segments for inspiration — yours can look completely different!

![Example caterpillar](media/caterpillar.svg){:height="50%" width="50%"}{: style="border-style: inset"}

## Tips

Some useful `turtle` functions:

- `turtle.circle(radius)` — draws a full circle counterclockwise
- `turtle.begin_fill()` / `turtle.end_fill()` — fill a shape with `turtle.fillcolor("color")`
- `turtle.penup()` / `turtle.pendown()` / `turtle.goto(x, y)` — move without drawing
- `turtle.setheading(angle)` — point the turtle in a direction (0 = right, 90 = up)
- `turtle.forward(distance)` — move the turtle forward (handy for antennae!)

{: .callout.callout-info}
> #### Automated feedback
>
> Your code will be checked for errors and common code issues, but the correctness of your drawing is not verified automatically. Make sure to look at your own output and verify that it matches what the assignment asks for.
