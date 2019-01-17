#!/usr/bin/env python

#example of inheritance


class Shape(object):
        import turtle

        #create a global variable called "t"
        global t
        t = turtle.Pen()

        def __init__(self, height, length, numSides):
                self.length = length
                self.height = height
                self.numSides = numSides

        def contract(self, amount):
                self.length = self.length / amount
                self.height = self.height / amount
                return self.length, self.height
        
        def drawShape(self, x, y, colour, fill, line):
                t.color(fill)
                t.pencolor(colour)
                t.width(line)
                t.penup()
                t.goto(x,y)
                t.pendown()

                t.begin_fill()
                count = self.numSides
                while count > 0:
                        t.forward(self.length)
                        t.right(self.angle())
                        count -= 1
                t.end_fill()
                t.penup()


class Rectangle(Shape):
        def area(this):
                return this.length * this.height

        def perimeter(this):
                return this.length * 2 + this.height * 2

        def angle(this):
                return 360 / this.numSides

        

class Triangle(Shape):
        def area(this):
                return (this.length * this.height) / 2

        def perimeter(this):
                area = "calculate area"
                return area

        def angle(this):
                return 360 / this.numSides



myShape1 = Rectangle(50, 100, 4)
myShape2 = Triangle(50, 100, 3)
myShape3 = Triangle(50, 50, 3)

'''
print(myShape1.area())
print(myShape2.area())
print(myShape3.area())
'''

myShape1.drawShape(0, 0,"blue","red", 3)
myShape2.drawShape(20, 20,"blue","red", 3)


