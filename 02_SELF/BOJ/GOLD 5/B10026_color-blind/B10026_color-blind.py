import sys
from collections import deque
#sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(alp, si, sj, flag):
    q = deque()
    q.append((si, sj))

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]: continue
            if flag == 'seen':
                if arr[ni][nj] != alp: continue
            else:
                if arr[ni][nj] == alp: continue
            q.append((ni, nj))
            visited[ni][nj] = 1


n = int(input())
arr = [list(map(str, input().rstrip())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
seen_cnt = 0
b_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            check(arr[i][j], i, j, 'seen')
            if arr[i][j] == 'B': b_cnt +=1
            else: seen_cnt += 1

visited = [[0]*n for _ in range(n)]
blind_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                check('B', i, j, 'blind')
                blind_cnt += 1

print(b_cnt+seen_cnt, b_cnt+blind_cnt)