import sys

sys.stdin = open('input.txt')


# input
N, M, K = map(int, input().split())
sharks = [0] * (M+1)
smells = [[[] for _ in range(N)] for _ in range(N)]
for nn in range(N):
    inp = list(map(int, input().split()))
    for mm in range(N):
        if inp[mm] > 0:
            sharks[inp[mm]] = [nn, mm]

dirs = list(map(int, input().split()))
for n in range(1, M+1):
    sharks[n].append(dirs[n-1]-1)

priority = [[] for _ in range(M+1)]
for d1 in range(4):
    for d2 in range(4):
        inp = list(map(lambda x: int(x)-1, input().split()))
        priority[d1+1].append(inp)
