#!/usr/bin/env python

class poly(object):
    def __init__(self, numSides, length, width, fill, colour):
        self.length = length
        self.width = width
        self.fill = fill
        self.colour = colour
        self.numSides = numSides
        description = "This shape has not been described yet"
    
    def describe(self, text):
        self.description = text
    
    def scaleSize(self, scale):
        self.length = self.length * scale
        self.width = self.width * scale

    def extAngle(self):
        angle = 360 / self.numSides
        return int(angle)

    def intAngle(self):
        angle = 180 - (360 / self.numSides)
        return int(angle)

    def drawShape(self, x, y, angle):
        import turtle
        t = turtle.Pen()

        t.color(self.fill)
        t.pencolor(self.colour)
        t.width(5)
        
        t.goto(x, y)

        
        t.pendown()
        t.begin_fill()

        count = self.numSides
        while count > 0:
            t.forward(self.length)
            t.right(angle)
            count -= 1
        
        t.penup()
        t.end_fill()
        



rectangle = poly(4, 100, 45, "red", "blue")


print(rectangle.width)

print(rectangle.colour)

rectangle.drawShape(0,0, rectangle.extAngle())
