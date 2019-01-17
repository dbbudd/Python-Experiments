    def __iter__(self):
        if self:
            if self.leftChild:
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.rightChild:
                for elem in self.rightChild:
                    yield elem
