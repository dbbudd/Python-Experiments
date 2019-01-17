def dijkstra(G,start):
    PQ = PriorityQueue()
    start.setDistance(0)
    PQ.buildHeap([(v.getDistance(),v) for v in G])        
    while not PQ.isEmpty():
        w = PQ.delMin()
        for v in w.getAdj():
            newDist = w.getDistance() + w.getCost(v)
            if newDist < v.getDistance():
                v.setDistance( newDist )
                v.setPred(w)
                PQ.decreaseKey(v,newDist)
