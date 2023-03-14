import sys
from collections import deque

sys.stdin = open('input.txt')

for _ in range(2):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]  # 벽을 안부쉈을 때, 부쉈을 때
    visited[0][0] = [0, 0]
    q = deque()
    q.append((0, 0, 0, 0))  # flag = 0, 아직 부순 벽이 없는 것

    while q:
        ci, cj, flag, cnt = q.popleft()

        next_flag = flag
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if flag and arr[ni][nj] == 1: continue  # 이미 벽을 부순 상태
            if not flag and arr[ni][nj] == 1:  # 벽 부숨
                next_flag = 1
            if visited[ni][nj][flag] == -1:
                visited[ni][nj][flag] = cnt + 1
                q.append((ni, nj, next_flag, cnt+1))

    # 둘다 -1 경로가 있는 경우
    # v1, v2 = visited[n-1][m-1]
    # if v1 > 0 and v2 > 0:
    #     print(min(v1, v2)+1)
    # else:  # 한쪽은 음수인경우
    #     res = v1 if v1 > 0 else v2
    #     if res > 0: res += 1
    #     print(res)

    for e in visited:
        print(e)
    print()