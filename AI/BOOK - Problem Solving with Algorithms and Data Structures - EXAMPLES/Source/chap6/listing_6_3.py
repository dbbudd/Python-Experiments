def buildGraph():
    d = {}
    g = Graph()    
    wfile = file('words.dat')
    # create buckets of words that differ by one letter.
    for line in wfile:
        word = line[0:5]
        for i in range(5):
            bucket = word[0:i] + '_' + word[i+1:5]
            if d.has_key(bucket):
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket.
    for i in d.keys():
        for j in d[i]:
            for k in d[i]:
                if j != k:
                    g.addEdge(j,k)
    return g

