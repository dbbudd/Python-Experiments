class HashTable:
    def __init__(self,size):
        self.slots = [None] * size
        self.data = [None] * size
