def __init__(self,key,val,parent=None,
                          left=None,right=None):
    self.key = key
    self.payload = val
    self.leftChild = left
    self.rightChild = right
    self.parent = parent
