    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:               t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
