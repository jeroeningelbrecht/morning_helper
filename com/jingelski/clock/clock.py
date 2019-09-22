import turtle
import time
from com.jingelski.weather.weather_man import WeatherMan


class Clock:

    def __init__(self):
        self.weather_man = WeatherMan()

        # initiate the window
        self.window = turtle.Screen()
        self.window.bgcolor("#CCCCCC")
        self.window.setup(width=1024, height=768)
        self.window.title("Morning Helper")
        self.window.tracer(0)  # disable the clock animation

        # create the drawing pen
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(3)

        while True:
            h = int(time.strftime("%I"))
            m = int(time.strftime("%M"))
            s = int(time.strftime("%s"))

            self._draw_clock(h, m, s)
            self.window.update()

            time.sleep(1)

            self.pen.clear()

    def _draw_clock_face(self) -> None:
        self.pen.up()
        self.pen.goto(0, 210)
        self.pen.setheading(180)
        self.pen.color("green")
        self.pen.pendown()
        self.pen.circle(210)

    def _draw_clock_lines(self) -> None:
        # draw the lines
        self.pen.up()
        self.pen.goto(0, 0)
        self.pen.setheading(90)

        for hour in range(12):

            # clock radius is 210
            # go forward 190
            # pen down and draw a line of 20 long to get to the 'edge circle' of the clock

            self.pen.fd(190)
            self.pen.pendown()
            # every line has a length of 20
            self.pen.fd(20)
            self.pen.penup()

            self.pen.fd(10)
            # self.pen.write(str(hour))

            self.pen.goto(0, 0)
            # 360°/12 lines = 1 line per 30°
            self.pen.rt(30)

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
        self.pen.color("black")
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

    def _write_temperature(self):
        # write the temperatures
        self.pen.up()
        self.pen.goto(210, 210)
        self.pen.write(str(self.weather_man.current_temperature) + ' °C')

    def _draw_clock(self, h, m, s):
        self._draw_clock_face()
        self._draw_clock_lines()
        self._draw_hour_hand(h)
        self._draw_minute_hand(m)
        self._draw_second_hand(s)
        self._write_temperature()
