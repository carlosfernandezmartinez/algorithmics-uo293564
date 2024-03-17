import Helper as help

def prim(edges):
    exploredNodes = [0]

    totalCost = 0

    while(len(exploredNodes) != len(edges)):
        mini = -1
        minj = -1
        minCost = 2**31-1
        for i in range(len(edges)):
            for j in range (i + 1, len(edges[0])):
                if (i in exploredNodes and j not in exploredNodes and edges[i][j] < minCost):
                    mini = i
                    minj = j
                    minCost = edges[i][j]
                elif (i not in exploredNodes and j in exploredNodes and edges[i][j] < minCost):
                    mini = j
                    minj = i
                    minCost = edges[i][j]
        totalCost += minCost
        exploredNodes.append(minj)
        print("From node ", mini, " to ", minj, " cost: ", minCost)

    print("Total cost of the minimum cost graph: ", totalCost)