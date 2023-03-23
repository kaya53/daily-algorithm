import sys
from collections import deque

sys.stdin = open('sample_input.txt')

pipe_dir = [0, [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
candidiate = [[1,2,5,6], [1,2,4,7], [1,3,4,5], [1,3,6,7]]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input())
for tc in range(1, t+1):
    n, m, si, sj, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    q = deque()
    # 시작 좌표, 시작 좌표 파이프 종류, cnt
    q.append((si, sj, arr[si][sj]))
    # 방문 표시
    arr[si][sj] = -1
    flag = False
    time = cnt = 0
    while q:
        time += 1
        for _ in range(len(q)):
            ci, cj, pipe = q.popleft()
            if time > l:
                flag = True
                break
            cnt += 1  # 개수는 시간 이내일 때만 늘려주기
            now_d = pipe_dir[pipe]
            for d in now_d:
                ni, nj = ci + delta[d][0], cj + delta[d][1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                if arr[ni][nj] <= 0: continue
                if arr[ni][nj] in candidiate[d]:
                    q.append((ni, nj, arr[ni][nj]))
                    arr[ni][nj] = -1  # 방문 표시
        if flag:
            break
    print(f'#{tc} {cnt}')