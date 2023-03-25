import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def check(choice, adj):
    global mmin, ls

    c1, c2 = choice
    res = 0
    for i in range(1, n+1):  # 열은 고정하고 행을 순회한다
        res += min(adj[i][c1], adj[i][c2])
    if mmin > res:
        mmin = res
        ls = list(choice)

def comb(idx):
    if idx == 2:
        check(choice, adj)
        return
    for nnext in range(idx, n):
        choice[idx] = nnext + 1
        comb(idx+1)
        choice[idx] = 0

def fw(adj):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    return adj


n, m = map(int, input().split())
INF = int(1e9)
adj = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: adj[i][j] = 0

choice = [0, 0]
ls = []
mmin = int(1e9)
adj = fw(adj)
comb(0)
print(*ls, mmin*2)
for a in adj:
    print(a)