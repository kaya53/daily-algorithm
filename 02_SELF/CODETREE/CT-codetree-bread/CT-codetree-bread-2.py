import sys
from collections import deque


input = sys.stdin.readline

def find_basecamp(conv):
    si, sj = conv
    # bfs로 가장 가까운 베캠 찾기; 1이 그 대상
    q = deque()
    q.append((si, sj))
    visited = [[0] * n for _ in range(n)]
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            # 인덱스 밖
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            # 베캠이나 편의점이 있는 곳, bfs 돌다가 방문한 곳
            if arr[ni][nj] == -1 or visited[ni][nj]: continue
            if arr[ni][nj] == 1:  # 가장 가까운 베이스 캠프
                return ni, nj
            q.append((ni, nj))
            visited[ni][nj] = 1


def move(q, conv):
    global cnt

    visited = [[0] * n for _ in range(n)]
    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                # 인덱스 밖
                if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                if arr[ni][nj] == -1 or visited[ni][nj]: continue
                if (ni, nj) == (conv[0], conv[1]):
                    arr[ni][nj] = -1  # 편의점 세우기
                    cnt += 1
                    return []
                q.append((ni, nj))
                visited[ni][nj] = 1
        return q


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
conv = [0] + [list(map(lambda x: x-1, map(int, input().rstrip().split()))) for _ in range(m)]

base_q = [0] * (m+1)
time = cnt = 0
while True:
    time += 1
    if time <= m:
        bi, bj = find_basecamp(conv[time])
        arr[bi][bj] = -1
        base_q[time] = deque([(bi, bj)])
    # 한 칸씩 이동하기; 1번부터 차례로 이동
    for no in range(1, m+1):
        if no == time: continue
        if not base_q[no]: continue
        base_q[no] = move(base_q[no], conv[no])

    if cnt == m:
        print(time)
        break