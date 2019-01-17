import turtle
def draw_tree(length, depth):
    t.forward(length)
    if depth > 1:
        t.left(45)
        draw_tree(length/2, depth-1)
        t.left(90)
        draw_tree(length/2, depth-1)
        t.right(135)
        t.right(180)
        t.forward(length)

t = turtle.Turtle()
t.penup()
t.goto(0,-100)
t.pendown()
t.left(90)
t.speed(0)

draw_tree(160,7)
turtle.exitonclick()