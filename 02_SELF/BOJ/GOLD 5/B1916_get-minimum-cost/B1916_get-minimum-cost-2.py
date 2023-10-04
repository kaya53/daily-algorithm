import sys

sys.stdin = open('input.txt')

INF = int(1e9)

def solution():
    n = int(input())
    m = int(input())

    graph = [[INF] * n for _ in range(n)]
    for z in range(n):
        graph[z][z] = 0
    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s-1][e-1] = c

    start, end = map(lambda x: int(x)-1, input().split())

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph[start][end]



print(solution())
