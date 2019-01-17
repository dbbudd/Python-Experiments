import turtle

def floor(x, y):
    if x > y:
        return x
    return y


def draw_fern(length1, angle1, length2, angle2, depth):
    flip = 1
    for i in range(0, length2):
        t.left(angle2)
        t.forward(length1)
        if depth > 1:
            t.left(angle1 * flip)
            draw_fern(floor((length1 /3) - (i / 2), 1), angle1 * flip, floor(length2 - i, 1), angle2 * flip, depth - 1)
            t.left(180 - angle1 * flip)
        flip = flip * -1
    
    t.left(180)
    
    for i in range(0, length2):
        t.forward(length1)
        t.right(angle2)

t = turtle.Turtle()

t.penup()
t.goto(0, -100)
t.pendown()
t.left(90)
t.speed(0)
draw_fern(40,60,8,4,1)

turtle.exitonclick()