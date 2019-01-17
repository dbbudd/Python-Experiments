def delete_key(self,key):
	if self.key == key:	 # do the removal
		if not (self.leftChild or self.rightChild):
			if self == self.parent.leftChild:
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif (self.leftChild or self.rightChild) and \
				 (not (self.leftChild and self.rightChild)):
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
		else:  # replace self with successor
			succ = self.findSuccessor()
			succ.spliceOut()
			if self == self.parent.leftChild:
				self.parent.leftChild = succ
			else:
				self.parent.rightChild = succ
			succ.leftChild = self.leftChild
			succ.rightChild = self.rightChild				
	else: # continue looking
		if key < self.key:
			if self.leftChild:
				self.leftChild.delete_key(key)
			else:
		else:
			if self.rightChild:
				self.rightChild.delete_key(key)
			else:
				print "trying to remove a non-existant node"
