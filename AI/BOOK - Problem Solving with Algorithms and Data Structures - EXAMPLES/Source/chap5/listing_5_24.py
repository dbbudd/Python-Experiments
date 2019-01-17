elif (self.leftChild or self.rightChild) \
      and (not (self.leftChild and self.rightChild)):
    print "removing a node with one child"
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
