import time

def sumOfN(n):
   start = time.clock()

   sum = 0
   for i in range(1,n+1):
      sum = sum + i

   end = time.clock()

   return sum,end-start
