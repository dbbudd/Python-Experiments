    def search(self,item):
      startslot = self.hashfunction(item,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == item:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,item):
        return self.search(item)

    def __setitem__(self,item,data):
        self.store(item,data)

