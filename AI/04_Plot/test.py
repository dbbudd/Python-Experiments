import turtle

t = turtle.Pen()

'''
def square():
    for i in range(4):
        t.forward(100)
        t.right(90)
        

for i in range(4):
    square()
    t.right(30)
'''

turtle.setup(600,400)
myWindow = turtle.Screen()

def Japan():
    #set background colour
    myWindow.bgcolor("white")
    
    #draw shape
    t.goto(0,-100)
    t.color("red")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    
    
def snowflake(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        snowflake(length/3, depth - 1)
        t.right(60)
        snowflake(length/3, depth - 1)
        t.left(120)
        snowflake(length/3, depth - 1)
        t.right(60)
        snowflake(length/3, depth - 1)

#snowflake(500, 4)

def drawSpiral(length):
    if length > 0:
        t.forward(length)
        t.right(90)
        drawSpiral(length - 5)
        
#drawSpiral(100)


def koch(order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(order-1, size/3)
           t.left(angle)

def drawTriangles(sides):
    if sides > 0:
        t.forward(sides)
        t.right(120)
        t.forward(sides)
        t.right(120)
        t.forward(sides)
        t.right(120)
        drawTriangles(sides - 50)

#drawTriangles(500)

t.speed(1000)
def tree(branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 5)
        t.left(40)
        tree(branchLen - 15)
        t.right(20)
        t.backward(branchLen)

#tree(100)


def fibonacci_word(n) :
    if n < 0 :
        return None
    elif n == 0 :
        return [1]
    elif n == 1 :
        return [0]
    else :
        f_n_1 = fibonacci_word(n - 1)
        f_n_2 = fibonacci_word(n - 2)
        return f_n_1 + f_n_2
 
def draw_fibonacci_word(fib_word, step = 10) :
    import turtle
    turtle.setworldcoordinates(0, 0, 800, 600)
    turtle.Screen()
    turtle.home()
 
    for i, symbol in enumerate(fib_word) :
        turtle.forward(step)
        if symbol == 0 and i % 2 == 0 :
            turtle.left(90)
        elif symbol == 0 and i % 2 == 1 :
            turtle.right(90)
            
    turtle.bye()
 
def main() :
    #n = int(input("Enter an integer for n:"))
    n = 100
    fib_word_n = fibonacci_word(n)
    draw_fibonacci_word(fib_word_n)
 
if __name__ == '__main__':
    main()

myWindow.exitonclick()

