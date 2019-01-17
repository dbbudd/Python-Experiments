def prim(G,start):
    PQ = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxint)
        v.setPred(None)
    start.setDistance(0)
    PQ.buildHeap([(v.getDistance,v) for v in G])
    while not PQ.isEmpty():
        u = PQ.delMin()
        for v in u.getAdj():
            if v in PQ and u.cost(v) < v.getDistance():
                v.setPred(u)
                v.setDistance(u.cost(v))
                PQ.decreaseKey((u.cost(v)))
