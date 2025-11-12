import turtle as t

t.speed(0)
t.hideturtle()

# Draw X-axis
t.penup()
t.goto(-200, 0)
t.pendown()
t.goto(200, 0)

# Draw Y-axis
t.penup()
t.goto(0, -200)
t.pendown()
t.goto(0, 200)

t.done()
