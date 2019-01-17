convertString = "0123456789ABCDEF"
rStack = Stack()

def toStr(n,base):
    if n < base:                 
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n%base])
        toStr(n / base,base)     
