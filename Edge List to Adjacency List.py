def convertToAdjList(n, edgeList):
    listt = [[] for _ in range(n)]
    for i , j in edgeList:
        listt[i].append(j)
        listt[j].append(i)
    return listt
