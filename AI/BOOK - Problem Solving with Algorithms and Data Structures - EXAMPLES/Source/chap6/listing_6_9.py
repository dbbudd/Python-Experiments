def dfs(theGraph):
    for u in theGraph:
        u.setColor('white')
        u.setPred(-1)
    time = 0
    for u in theGraph:
        if u.getColor() == 'white':
            dfsvisit(u)

def dfsvisit(s):
    s.setDistance(0)
    s.setPred(None)
    S = Stack()
    S.push(s)
    while (S.size() > 0):
        w = S.pop()
        w.setColor('gray')
        for v in w.getAdj():""
            if (v.getColor() == 'white'):
                v.setDistance( w.getDistance() + 1 )
                v.setPred(w)
                S.push(v)
        w.setColor('black')

