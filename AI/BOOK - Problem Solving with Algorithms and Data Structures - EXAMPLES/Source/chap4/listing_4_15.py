    def store(self,item,data):
      hashvalue = self.hashfunction(item,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = item
        self.data[hashvalue] = data
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None:
          nextslot = self.rehash(nextslot,len(self.slots))

        self.slots[nextslot]=item
        self.data[nextslot]=data

    def hashfunction(self,item,size):
             return item%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size
