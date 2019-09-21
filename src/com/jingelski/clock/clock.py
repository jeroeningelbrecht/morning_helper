import turtle
import time

window = turtle.Screen()
window.bgcolor("#CCCCCC")
window.setup(width=600, height=600)
window.title("Analoge klok")
window.tracer(0) # disable the clock animation

# create the drawing pen
pen = turtle.Turtle()

pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h, m, s, pen):
    # draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # draw the lines
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        # every line has a length of 20
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        # 360°/12 lines = 1 line per 30°
        pen.rt(30)

    # draw the hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    draw_clock(h, m, s, pen)
    window.update()

    time.sleep(1)

    pen.clear()

window.mainloop()
