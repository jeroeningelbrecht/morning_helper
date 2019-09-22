import turtle
import time
from com.jingelski.weather.weather_man import WeatherMan


def draw_clock_face(pen) -> None:
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)


def draw_clock_lines(pen) -> None:
    # draw the lines
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for hour in range(12):
        # clock radius is 210
        # go forward 190
        # pen down and draw a line of 20 long to get to the 'edge circle' of the clock

        pen.fd(190)
        pen.pendown()
        # every line has a length of 20
        pen.fd(20)
        pen.penup()

        pen.fd(15)
        pen.write(str((lambda: 12, lambda: hour)[hour != 0]()), font=("Arial", 10, "bold"))

        # draw the second marks in black
        pen.color("black")

        for second in range(4):
            pen.goto(0, 0)
            pen.rt(6)
            pen.fd(200)
            pen.pendown()
            pen.fd(10)
            pen.penup()

        # continue with the 5 minute marks in green
        pen.color("green")
        # 360°/60 lines = 1 line per 6° BUT 1 big line for every 5 mins and 4 smaller 'second' lines in between two
        # 5 minute lines
        pen.goto(0, 0)
        pen.rt(6)


class Clock:

    def __init__(self):
        self.weather_man = WeatherMan()

        # initiate the window
        self.window = turtle.Screen()
        self.window.bgcolor("#CCCCCC")
        self.window.setup(width=1024, height=768)
        self.window.title("Morning Helper")
        self.window.tracer(0)  # disable the clock animation

        # create the drawing pen for the dynamic part
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(3)

        # create a pen for the static part: the clock skeleton
        self.static_clock_turtle_pen = turtle.Turtle()
        self.static_clock_turtle_pen.hideturtle()
        self.static_clock_turtle_pen.speed(0)
        self.static_clock_turtle_pen.pensize(3)

        # draw the clock skeleton
        draw_clock_face(self.static_clock_turtle_pen)
        draw_clock_lines(self.static_clock_turtle_pen)

        # create a different turtle for the temperature information as this information only needs to get updated
        # once in a while
        self.temp_turtle_pen = turtle.Turtle()
        self.temp_turtle_pen.hideturtle()
        self.temp_turtle_pen.speed(0)
        self.temp_turtle_pen.pensize(3)
        self._write_temperature(self.temp_turtle_pen)

        while True:
            h = int(time.strftime("%I"))
            m = int(time.strftime("%M"))
            s = int(time.strftime("%s"))

            self._draw_clock(h, m, s)
            self.window.update()

            time.sleep(1)

            self.pen.clear()

    def _draw_hour_hand(self, h) -> None:
        # draw the hour hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("black")
        self.pen.setheading(90)
        angle = (h / 12) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(100)

    def _draw_minute_hand(self, m) -> None:
        # draw the minute hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("blue")
        self.pen.setheading(90)
        angle = (m / 60) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(150)

    def _draw_second_hand(self, s) -> None:
        # draw the second hand
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.color("red")
        self.pen.setheading(90)
        angle = (s / 60) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(100)

    def _write_temperature(self, pen):
        # write the temperatures
        pen.up()
        pen.goto(-350, 350)
        pen.write('TEMPERATUUR NU: ' + str(self.weather_man.current_temperature) + ' °C',
                  font=("Arial", 16, "bold"))
        pen.up()
        pen.goto(-350, 330)
        pen.write('MAXIMUM TEMPERATUUR VANDAAG: ' + str(self.weather_man.temperature_high) + ' °C',
                  font=("Arial", 16, "bold"))
        pen.up()
        pen.goto(-350, 310)
        pen.write('MINIMUM TEMPERATUUR VANDAAG: ' + str(self.weather_man.temperature_low) + ' °C',
                  font=("Arial", 16, "bold"))

    def _draw_clock(self, h, m, s):
        self._draw_hour_hand(h)
        self._draw_minute_hand(m)
        self._draw_second_hand(s)
