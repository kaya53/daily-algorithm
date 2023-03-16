import sys

sys.stdin = open('input.txt')

from collections import deque


def BFS(q):
    ei, ej = 0, 0
    while q:
        ci, cj = q.popleft()
        cnt = 0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            if arr[ni][nj] and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
        # 이 덩어리의 마지막 점을 어떻게 구할까
        if cnt == 0:
            ei, ej = ci, cj
    return ei, ej

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0]*n for _ in range(n)]

    res = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                ei, ej = BFS(q)
                res.append((abs(ei-i)+1, abs(ej-j)+1))
    ls = sorted(res, key=lambda x: [x[0]*x[1], x[0], x[1]])
    print(f'#{tc} {len(ls)}', end=' ')
    for elem in ls:
        print(*elem, end=' ')
    print()
