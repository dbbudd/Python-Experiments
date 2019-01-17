convertString = "0123456789ABCDEF"

def toStr(n,base):
   if n < base:              return convertString[n]
   else:
      return toStr(n / base,base) + convertString[n%base]   