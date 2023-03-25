import sys
from collections import deque
# sys.stdin = open('input.txt')

input = sys.stdin.readline

def bfs(no, c1, c2, visited):
    # 가다가 치킨집이 c1이나 c2이면 멈추기
    q = deque()
    q.append(no)
    dist = -1
    while q:
        dist += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == c1 or now == c2:
                return dist
            for nnext in range(1, n+1):
                if not adj[now][nnext] or visited[nnext]: continue
                q.append(nnext)


def find(choice):
    c1, c2 = choice
    res = 0
    for no in range(1, n+1):
        if no == c1 or no == c2: continue
        visited = [0]*(n+1)
        visited[no] = 1
        res += bfs(no, c1, c2, visited)

    return res

def comb(idx):
    global mmin, ls
    if idx == 2:
        res = find(choice)
        if mmin > res:
            mmin = res
            ls = list(choice)
        return
    for ni in range(idx, n):
        choice[idx] = ni+1
        comb(idx+1)
        choice[idx] = 0


n, m = map(int, input().split())
adj = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 1

choice = [0, 0]
mmin = int(1e9)
ls = []
comb(0)
print(*ls, mmin*2)
