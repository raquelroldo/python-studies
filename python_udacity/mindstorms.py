import turtle


def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("yellow","pink")
    brad.speed(5)
    brad.begin_fill()
    for i in range(1, 19):
        draw_square(brad)
        brad.right(20)
    brad.end_fill()
    # angie = turtle.Turtle()       # Draws circle
    # angie.color("green")
    # angie.speed(8)
    # angie.circle(50)
    # cnt = 0                       # Draws multiple circles
    # while cnt < 17:
    #     angie.right(20)
    #     angie.circle(100)
    #     cnt += 1
    #
    # trup = turtle.Turtle()        # Draws triangle
    # trup.color("blue")
    # trup.speed(4)
    # times = 0
    # while times < 3:
    #     trup.forward(90)
    #     trup.left(120)
    #     times += 1
    # cnt = 0                       # Draws multiple triangles
    # while cnt < 17:
    #     trup.right(20)
    #     cnt += 1
    #     for i in range(1, 4):
    #         trup.forward(90)
    #         trup.left(120)
    window.exitonclick()


draw_art()
