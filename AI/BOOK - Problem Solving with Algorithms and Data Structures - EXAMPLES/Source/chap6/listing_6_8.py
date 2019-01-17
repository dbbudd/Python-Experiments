def orderByAvail(n):
    resList = []
    for v in n.getAdj():
        if v.getColor() == 'white':
            c = 0
            for w in v.getAdj():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort()        return [y[1] for y in resList]   
