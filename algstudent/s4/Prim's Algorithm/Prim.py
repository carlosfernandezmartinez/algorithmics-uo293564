import Helper as help

def prim(edges):
    exploredNodes = [False] * len(edges)
    exploredNodes[0] = True

    totalCost = 0

    for k in range(len(edges) - 1):
        mini = -1
        minj = -1
        minCost = 2**31-1
        for i in range(len(edges)):
            for j in range (i + 1, len(edges[0])):
                if (exploredNodes[i] and not exploredNodes[j] and edges[i][j] < minCost):
                    mini = i
                    minj = j
                    minCost = edges[i][j]
                elif (not exploredNodes[i] and exploredNodes[j] and edges[i][j] < minCost):
                    mini = j
                    minj = i
                    minCost = edges[i][j]
        totalCost += minCost
        exploredNodes[minj] = True
        print("From node ", mini, " to ", minj, " cost: ", minCost)

    print("Total cost of the minimum cost graph: ", totalCost)