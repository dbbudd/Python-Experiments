else:  
    succ = self.findSuccessor()
    succ.spliceOut()
    if self == self.parent.leftChild:
        self.parent.leftChild = succ
    else:
        self.parent.rightChild = succ
    succ.leftChild = self.leftChild
    succ.rightChild = self.rightChild               
