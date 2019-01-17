def listsum(l):
    if len(l) == 1:                       return l[0]
    else:
        return l[0] + listsum(l[1:])  