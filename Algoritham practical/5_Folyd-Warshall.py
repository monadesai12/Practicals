# Number of vertices
V = 4
INF = 99999

# Algorithm 
def floydWarshall(graph):
    dist = list(map(lambda p: list(map(lambda q: q, p)), graph))

    # Adding vertices individually
    for r in range(V):
        for p in range(V):
            for q in range(V):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    sol(dist)

# Printing the output
def sol(dist):
    for p in range(V):
        for q in range(V):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")

graph = [[0,5,INF,10], 
             [INF,0,3,INF], 
             [INF, INF, 0,   1], 
             [INF, INF, INF, 0] 
        ]
floydWarshall(graph)


