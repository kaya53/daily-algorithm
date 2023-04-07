import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_basecamp(conv):  # 도착지인 편의점
    ei, ej = conv
    min_dist = 31
    ri, rj = 0, 0
    for si, sj in basecamp:
        visited = [[0] * N for _ in range(N)]
        q = deque()
        q.append((si, sj, 0))
        visited[si][sj] = 1
        while q:
            ci, cj, dist = q.popleft()
            if dist >= min_dist: break
            if (ci, cj) == (ei, ej) and arr[ci][cj] != -1:
                if min_dist > dist:
                    min_dist = dist
                    ri, rj = si, sj
                    break
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == -1 or visited[ni][nj]: continue
                q.append((ni, nj, dist+1))
                visited[ni][nj] = 1

    arr[ri][rj] = -1
    basecamp.remove((ri, rj))
    return ri, rj


def move(q, conv):
    global cnt
    moved = [[0] * N for _ in range(N)]
    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == -1 or moved[ni][nj]: continue
                # if (ni, nj) in moved: continue
                if (ni, nj) == (conv[0], conv[1]):
                    arr[ni][nj] = -1  # 편의점 세우기
                    cnt += 1
                    return
                q.append((ni, nj))
                moved[ni][nj] = 1
        return


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
basecamp = []
for nn in range(N):
    inp = list(map(int, input().rstrip().split()))
    arr[nn] = inp
    for mm in range(N):
        if inp[mm] == 1: basecamp.append((nn, mm))

conv = [list(map(lambda x: int(x)-1, input().rstrip().split())) for _ in range(M)]

# print(basecamp)
base_q = [deque() for _ in range(M)]
# moved_set = [set() for _ in range(M)]
time = -1
cnt = 0
while True:
    time += 1
    # 한 칸씩 이동
    for pp_no in range(M):
        # if pp_no == time: continue  # 지금 막 베캠에 들어온 i
        if not base_q[pp_no]: continue  # 아직 격자에 들어오지 않은 i or 이미 편의점을 찾은 i
        move(base_q[pp_no], conv[pp_no])
    if time < M:
        # print('time', time)
        bi, bj = find_basecamp(conv[time])
        base_q[time].append((bi, bj))

    if cnt == M:
        print(time+1)
        break
