import turtle


def draw_square(some_turtle):      # Draws a square
    for i in range(1,5):
        some_turtle.backward(50)
        some_turtle.left(90)


def draw_art():          # Draws multiple square
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("purple")
    brad.speed(4)
    draw_square(brad)
    brad.backward(50)
    brad.right(90)
    brad.forward(100)
    brad.backward(50)
    brad.left(45)
    brad.forward(80)

    window.exitonclick()


draw_art()