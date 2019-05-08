import turtle
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("purple")

    times = 0
    while times < 4:
        brad.forward(100)
        brad.right(90)
        times += 1
    
    angie = turtle.Turtle()
    angie.color("yellow")
    angie.circle(100)

    trup = turtle.Turtle()
    trup.color("blue")
    
    times = 0
    while times < 3:
        trup.forward(90)
        trup.left(120)
        times +=1

    window.exitonclick()



draw_art()