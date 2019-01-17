   def __cmp__(self,otherfraction):

        num1 = self.num*otherfraction.den
        num2 = self.den*otherfraction.num

        if num1 < num2:
           return -1
        else:
           if num1 == num2:
              return 0
           else
              return 1
