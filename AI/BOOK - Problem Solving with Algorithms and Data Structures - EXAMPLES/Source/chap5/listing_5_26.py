    def findSuccessor(self):
        succ = None
        if self.rightChild:
            succ = self.rightChild.findMin()
        else:
            if self.parent.leftChild == self:
                succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findSuccessor()
                self.parent.rightChild = self
        return succ

    def findMin(self):
        n = self
        while n.leftChild:
            n = n.leftChild
        print 'found min, key = ', n.key
        return n
