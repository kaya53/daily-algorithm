# 118372kb	196ms
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
s_map = [[list() for _ in range(N)]for _ in range(N)]
l_map = [[0]*N for _ in range(N)]
dr = (-1,1,0,0)
dc = (0,0,-1,1)

for _ in range(M):
    r,c,r2,c2 = map(lambda a:int(a)-1,input().rstrip().split())
    s_map[r][c].append((r2,c2))

def solve():
    print(bfs())

def bfs():
    que = deque()
    visited = [[0]*N for _ in range(N)]

    l_map[0][0] = 1
    visited[0][0] = 1
    que.append((0,0))
    cnt = 1

    while que:
        r,c = que.popleft()
        for sr,sc in s_map[r][c]: # 현재 방에서 켤수 있는 방 모두 켜기
            if visited[sr][sc] == 1 and l_map[sr][sc] == 0: que.append((sr,sc))
            if l_map[sr][sc] == 0 :
                l_map[sr][sc] = 1
                cnt += 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr<0 or nr>=N or nc<0 or nc>=N or visited[nr][nc] : continue
            visited[nr][nc] = 1
            if l_map[nr][nc]:
                visited[nr][nc] = 1
                que.append((nr,nc))
    return cnt
solve()