import turtle


screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)


def draw_triangle():
    pen.color("red")
    for _ in range(3):
        pen.forward(100)
        pen.left(120)


def draw_hexagon():
    pen.color("blue")
    for _ in range(6):
        pen.forward(70)
        pen.left(60)


def draw_star():
    pen.color("green")
    for _ in range(5):
        pen.forward(100)
        pen.right(144)


pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_triangle()


pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_hexagon()


pen.penup()
pen.goto(200, 0)
pen.pendown()
draw_star()


pen.hideturtle()
screen.mainloop()
