import turtle
t = turtle.Pen()
t.penup()

def star(n, d, s, colour):
    '''
    n is the number of spikes on the star
    d is the SMALLEST number of arcs between two connected spikes
    s is the sidelength
    '''

    vertex_angle = 180 / (n / (n - 2 * d))
    base_angle = (180 - vertex_angle) / 2
    interior_polygon_angle = (n - 2) * 180 / n
    outside_angle = 360 - (interior_polygon_angle + 2 * base_angle)
    
    t.color(colour)
    t.pencolor(colour)
    t.setheading(270 + vertex_angle / 2)
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(s)
        t.left(180 - outside_angle)
        t.forward(s)
        t.right(180 - vertex_angle)
    t.end_fill()
    t.penup()


t.goto(-100,240)

for d in range(1,4):
    star(8, d, 20, 'black')
    t.setheading(0)
    t.forward(120)

t.goto(-100,120)

for d in range(1,4):
    star(7, d, 20, 'green')
    t.setheading(0)
    t.forward(120)

t.goto(-100,0)

for d in range(1,3):
    star(6, d, 20, 'blue')
    t.setheading(0)
    t.forward(100)

t.goto(-100,-100)   

for d in range(1,3):
    star(5, d, 20, 'red')
    t.setheading(0)
    t.forward(90)

t.hideturtle()

turtle.done()
