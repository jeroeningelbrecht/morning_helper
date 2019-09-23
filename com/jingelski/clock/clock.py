import turtle
import time
from com.jingelski.weather.weather_man import WeatherMan


def draw_clock_face(pen, clock_radius, start_x) -> None:
    pen.up()
    pen.goto(start_x, clock_radius)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(clock_radius)


def draw_clock_lines(pen, clock_radius, start_x) -> None:
    # draw the lines
    pen.up()
    pen.goto(start_x, 0)
    pen.setheading(90)

    for hour in range(12):
        # clock radius
        # go forward 190
        # pen down and draw a line of 20 long to get to the 'edge circle' of the clock

        pen.fd(clock_radius-40)
        pen.pendown()
        # every line has a length of 20
        pen.fd(40)
        pen.penup()

        pen.fd(20)
        pen.write(str((lambda: 12, lambda: hour)[hour != 0]()), font=("Arial", 16, "bold"))

        # draw the second marks in black
        pen.color("black")

        for second in range(4):
            pen.goto(start_x, 0)
            pen.rt(6)
            pen.fd(clock_radius - 10)
            pen.pendown()
            pen.fd(10)
            pen.penup()

        # continue with the 5 minute marks in green
        pen.color("green")
        # 360°/60 lines = 1 line per 6° BUT 1 big line for every 5 mins and 4 smaller 'second' lines in between two
        # 5 minute lines
        pen.goto(start_x, 0)
        pen.rt(6)


class Clock:

    MAX_WIDTH = 1600
    MAX_HEIGHT = 900

    CLOCK_RADIUS = 400
    HOUR_HAND_LENGTH = 200
    MINUTE_HAND_LENGTH = 300
    SECOND_HAND_LENGTH = 200

    CLOCK_START_X = -MAX_WIDTH / 2 + CLOCK_RADIUS + 30
    TEXT_START_X = 50

    def __init__(self):
        self.weather_man = WeatherMan()

        # initiate the window
        self.window = turtle.Screen()
        self.window.bgcolor("#CCCCCC")
        self.window.setup(width=self.MAX_WIDTH, height=self.MAX_HEIGHT)
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
        draw_clock_face(self.static_clock_turtle_pen, self.CLOCK_RADIUS, self.CLOCK_START_X)
        draw_clock_lines(self.static_clock_turtle_pen, self.CLOCK_RADIUS, self.CLOCK_START_X)

        # create a different turtle for the temperature information as this information only needs to get updated
        # once in a while
        self.temp_turtle_pen = turtle.Turtle()
        self.temp_turtle_pen.hideturtle()
        self.temp_turtle_pen.speed(0)
        self.temp_turtle_pen.pensize(3)

        # write temperature data
        self._write_temperature(self.temp_turtle_pen)

        # write precipitation and windspeed
        self._write_weather(self.temp_turtle_pen)

        while True:
            h = int(time.strftime("%I"))
            m = int(time.strftime("%M"))
            s = int(time.strftime("%S"))

            self._draw_clock(h, m, s)
            # update weather information every 30 mins
            if (m == 30 or m == 0) and s == 0:
                self.weather_man.update()
                self.weather_man.temperature_high = m
                self.temp_turtle_pen.clear()
                # write temperature data
                self._write_temperature(self.temp_turtle_pen)
                # write precipitation and windspeed
                self._write_weather(self.temp_turtle_pen)

            self.window.update()

            time.sleep(1)

            self.pen.clear()

    def _draw_hour_hand(self, h, m) -> None:
        # draw the hour hand
        self.pen.penup()
        self.pen.goto(self.CLOCK_START_X, 0)
        self.pen.color("black")
        self.pen.setheading(90)
        # hour + (minutes/60) => hour hand does not remain static for an entire hour but gradually moves along while the
        # minutes pass
        angle = ((h + m/60) / 12) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(self.HOUR_HAND_LENGTH)

    def _draw_minute_hand(self, m) -> None:
        # draw the minute hand
        self.pen.penup()
        self.pen.goto(self.CLOCK_START_X, 0)
        self.pen.color("blue")
        self.pen.setheading(90)
        angle = (m / 60) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(self.MINUTE_HAND_LENGTH)

    def _draw_second_hand(self, s) -> None:
        # draw the second hand
        self.pen.penup()
        self.pen.goto(self.CLOCK_START_X, 0)
        self.pen.color("red")
        self.pen.setheading(90)
        angle = (s / 60) * 360
        self.pen.rt(angle)
        self.pen.pendown()
        self.pen.fd(self.SECOND_HAND_LENGTH)

    def _write_temperature(self, pen):
        # write the temperatures
        pen.up()
        pen.goto(self.TEXT_START_X, 350)
        pen.write('TEMPERATUUR NU: ' + str(self.weather_man.current_temperature) + ' °C',
                  font=("Arial", 16, "bold"))
        pen.up()
        pen.goto(self.TEXT_START_X, 330)
        pen.write('MAXIMUM TEMPERATUUR VANDAAG: ' + str(self.weather_man.temperature_high) + ' °C',
                  font=("Arial", 16, "bold"))
        pen.up()
        pen.goto(self.TEXT_START_X, 310)
        pen.write('MINIMUM TEMPERATUUR VANDAAG: ' + str(self.weather_man.temperature_low) + ' °C',
                  font=("Arial", 16, "bold"))

    def _write_weather(self, pen):
        #write the precipitation probability
        pen.up()
        pen.goto(self.TEXT_START_X, 290)
        pen.write('KANS OP NEERSLAG KOMEND UUR: ' + str(self.weather_man.precipitationProbability) + '%',
                  font=("Arial", 16, "bold"))

        pen.up()
        pen.goto(self.TEXT_START_X, 270)
        pen.write('WINDSNELHEID NU: ' + str(self.weather_man.current_wind_speed) +'km/u',
                  font=("Arial", 16, "bold"))

    def _draw_clock(self, h, m, s):
        self._draw_hour_hand(h, m)
        self._draw_minute_hand(m)
        self._draw_second_hand(s)
