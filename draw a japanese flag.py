import turtle


def main():
    t = turtle.Turtle()
    t.hideturtle()
    rectangle(t, -500, 309, 1000, 618)
    redsun(t)
    write(t)


def rectangle(t, x, y, w, h, color1='white', color2='black'):
    t.fillcolor(color1)
    t.begin_fill()
    t.pencolor(color2)
    t.up()
    t.goto(x, y)
    t.down()
    t.goto(x + w, y)
    t.goto(x + w, y - h)
    t.goto(x, y - h)
    t.goto(x, y)
    t.end_fill()


def redsun(t):
    t.up()
    t.goto(0, 0)
    t.down
    t.dot(350, 'red')


def write(t):
    t.up()
    t.goto(0, -250)
    t.write('japanese flag', font=(30), align='center')


main()
turtle.done()
