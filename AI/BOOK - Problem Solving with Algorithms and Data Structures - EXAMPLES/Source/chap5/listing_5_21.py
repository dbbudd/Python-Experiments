def get(self,key):
    if key == self.key:
        return self.payload
    elif key < self.key:
        if self.leftChild:
            return self.leftChild.get(key)
        else:
            return None
    elif key > self.key:
        if self.rightChild:
            return self.rightChild.get(key)
        else:
            return None
    else:
        print 'error: this line should never be executed'

def __getitem__(self,key):
    return self.get(key) 
