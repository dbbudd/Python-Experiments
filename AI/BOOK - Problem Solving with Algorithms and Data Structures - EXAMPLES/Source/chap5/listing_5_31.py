    def percUp(self,i):
        while i > 0:
            if self.heapList[i] < self.heapList[i/2]:
               tmp = self.heapList[i/2]
               self.heapList[i/2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i/2

