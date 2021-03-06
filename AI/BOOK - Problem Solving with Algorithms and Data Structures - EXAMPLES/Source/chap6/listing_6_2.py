class Graph:
   def __init__(self):
      self.vertList = {}
      self.numVertices = 0
        
   def addVertex(self,key):
      self.numVertices = self.numVertices + 1
      newVertex = Vertex(key)
      self.vertList[key] = newVertex
      return newVertex
    
   def getVertex(self,n):
      if self.vertList.has_key(n):
         return self.vertList[n]
      else:
         return None

   def has_key(self,n):
       return self.vertList.has_key(n)
    
   def addEdge(self,f,t,c=0):
       if not self.vertList.has_key(f):
          nv = self.addVertex(f)
       if not self.vertList.has_key(t):
          nv = self.addVertex(t)
       self.vertList[f].addNeighbor(self.vertList[t],c)
    
   def getVertices(self):
       return self.vertList.values()
        
   def __iter__(self):
       return self.vertList.itervalues()
