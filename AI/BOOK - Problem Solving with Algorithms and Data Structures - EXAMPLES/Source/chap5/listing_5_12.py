    def preorder(self):
        print self.key
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
