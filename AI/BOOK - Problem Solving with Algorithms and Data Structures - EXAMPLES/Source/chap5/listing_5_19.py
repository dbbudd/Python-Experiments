def put(self,key,val):
    if key < self.key:
        if self.leftChild:
            self.leftChild.put(key,val)
        else:
            self.leftChild = TreeNode(key,val,self)
    else:
        if self.rightChild:
            self.rightChild.put(key,val)
        else:
            self.rightChild = TreeNode(key,val,self)
