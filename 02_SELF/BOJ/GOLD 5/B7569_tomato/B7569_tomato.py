# 230502 python 2100ms pypy 1124ms

# arr을 3차원 배열로 만들지 말고 2차원으로 받아서 박스가 바뀌는 건 (-n, 0), (n, 0) 이런 식으로 봐줘도 됨
# => 같은 로직에서 시간이 훨씬 덜 걸림


import sys

sys.stdin = open('input.txt')

from collections import deque


def solve(q):
    global zeros

    day = -1
    while q:
        day += 1
        for _ in range(len(q)):
            c_box, ci, cj = q.popleft()

            # 이전 박스, 다음 박스
            for n_box in [c_box-1, c_box+1]:
                if n_box < 0 or n_box >= H or arr[n_box][ci][cj] or visited[n_box][ci][cj]: continue
                q.append((n_box, ci, cj))
                visited[n_box][ci][cj] = 1
                zeros -= 1

            # 상하좌우
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[c_box][ni][nj] or visited[c_box][ni][nj]: continue
                q.append((c_box, ni, nj))
                visited[c_box][ni][nj] = 1
                zeros -= 1
    if zeros: return -1
    return day


# for _ in range(3):
M, N, H = map(int, input().split())
arr = [[] for _ in range(H)]

visited = [[[0]*M for _ in range(N)] for _ in range(H)]
zeros = 0

que = deque()
for h in range(H):
    for r in range(N):
        inp = list(map(int, input().split()))
        arr[h].append(inp)
        zeros += inp.count(0)
        for c, citem in enumerate(inp):
            if citem == 1:
                que.append((h, r, c))
                visited[h][r][c] = 1

if zeros:
    print(solve(que))
else:
    print(0)





