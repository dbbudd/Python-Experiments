def spliceOut(self):
    if (not self.leftChild and not self.rightChild):
        if self == self.parent.leftChild:
            self.parent.leftChild = None
        else:
            self.parent.rightchild = None
    elif (self.leftChild or self.rightChild):
        if self.leftChild:
            if self == self.parent.leftChild:
                self.parent.leftChild = self.leftChild
            else:
                self.parent.rightChild = self.leftChild
        else:
            if self == self.parent.leftChild:
                self.parent.leftChild = self.rightChild
            else:
                self.parent.rightChild = self.rightChild
