class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print self.num,"/",self.den

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                     self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum/common,newden/common)

    def __cmp__(self,otherfraction):
        num1 = self.num*otherfraction.den
        num2 = self.den*otherfraction.num
        if num1 < num2:
    	     return -1
    	  else:
    	     if num1 == num2:
    	        return 0
    	     else:
    	        return 1
