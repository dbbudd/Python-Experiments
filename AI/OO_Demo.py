#!/usr/bin/env python

class Shape(object):
    def __init__(self, height, length, numSides, colour):
        self.length = length
        self.height = height
        self.numSides = numSides
        self.colour = colour
    
    def draw(self):
        import turtle
        t = turtle.Pen()
        angle = 360/self.numSides
        t.color(self.colour)
        
        for i in range(self.numSides):
            t.forward(self.length)
            t.right(angle)

class Rectangle(Shape):
    def area (this):
        return this.length * this.height


class Triangle(Shape):
    def area(this):
        return(this.length * this.height) / 2






#instantiate (create a new instance of an object)
myShape1 = Rectangle(50,100, 4, "blue")
myShape2 = Triangle(100, 100, 3, "red")

#reference properties
print(myShape1.numSides)
print(myShape2.numSides)

#call inherited methods from Shape object
myShape1.draw()
myShape2.draw()

#call own methods
myShape1.area()
myShape2.area()

