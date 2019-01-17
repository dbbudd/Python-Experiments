def knightTour(n,path,u,limit): 
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = orderByAvail(u)              i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1,                                            path, 
                                      nbrList[i],
                                      limit)    
            if not done:  # prepare to backtrack
                path.remove(u)
                u.setColor('white')
        else:
            done = True
        return done
