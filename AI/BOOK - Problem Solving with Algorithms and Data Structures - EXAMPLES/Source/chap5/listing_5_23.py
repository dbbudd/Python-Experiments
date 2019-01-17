if not (self.leftChild or self.rightChild):
    print "removing a node with no childrend"
    if self == self.parent.leftChild:
        self.parent.leftChild = None
    else:
        self.parent.rightChild = None
