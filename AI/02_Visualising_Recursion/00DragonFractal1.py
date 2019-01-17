import turtle

def dragon_build(turtle_string, n):
    """ Recursively builds a draw string. """
    """ defining f, +, -, as additional rules that don't do anything """
    rules = {'x':'x+yf', 'y':'fx-y','f':'f', '-':'-', '+':'+'}
    turtle_string = ''.join([rules[x] for x in turtle_string])
    if n > 1: return dragon_build(turtle_string, n-1)
    else: return turtle_string

def dragon_draw(size):
    """ Draws a Dragon Curve of length 'size'. """
    turtle_string = dragon_build('fx', size)
    for x in turtle_string:
        if x == 'f': turtle.forward(20)
        elif x == '+': turtle.right(90)
        elif x == '-': turtle.left(90)

def main():
    n = int(input("Size of Dragon Curve (int): "))
    dragon_draw(n)

if __name__ == '__main__': main()