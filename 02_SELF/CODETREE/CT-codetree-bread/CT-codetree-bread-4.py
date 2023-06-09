# 230605 python 119ms => 1시간 소요
# bfs 큐 관리
# - 한 턴에 한 칸씩 움직이기 때문에 가능한 큐를 모두 전역에서 관리해야 한다
# - (+) 각 큐에 대한 visited도 모두 전역으로 관리해야함 => 이전 턴에서 간 곳 안가게 하기 위함
# - 사실 매 턴마다 한 칸씩마나 가기 때문에 굳이 전역으로 관리해 줄 필요는 없음
import sys

sys.stdin = open('input.txt')

from collections import deque


def move(q, p_no):
    global remain
    visited = set()
    ei, ej = convenient[p_no]

    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()

            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == -1 or (ni, nj) in visited: continue
                q.append((ni, nj))
                visited.add((ni, nj))
                if (ni, nj) == (ei, ej):  # 편의점 도착
                    remain -= 1
                    # 못지나감 마킹
                    arr[ei][ej] = -1
                    # in_arr 큐 None으로 만들기
                    in_arr[p_no] = None
                    return
        break


def into_basecamp(si, sj):
    # si, sj: time번째 사람이 가고 싶은 베캠
    visited = [[0] * N for _ in range(N)]
    q = deque([(si, sj)])
    visited[si][sj] = 1
    candidate = []  # 갈 수 있는 베캠 후보군

    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()

            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                # 인덱스 밖, 지나갈 수 없다고 마킹된 곳, 방문했던 곳 => continue
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == -1 or visited[ni][nj]: continue
                if arr[ni][nj] == 1:  # 베캠 도착
                    candidate.append((ni, nj))
                    continue
                q.append((ni, nj))
                visited[ni][nj] = 1
        if candidate:
            candidate.sort()  # 행, 열 순으로 정렬
            ri, rj = candidate[0]
            arr[ri][rj] = -1  # 못 지나가는 곳 마킹
            in_arr[time].append((ri, rj))  # time: 전역 변수
            return


delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상좌우하
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
convenient = [None] + [(0, 0) for _ in range(M)]
for m in range(1, M+1):
    convenient[m] = tuple(map(lambda x: int(x)-1, input().split()))

remain = M
time = 0
in_arr = [None] +[deque() for _ in range(M)]
# all_visited = [None] + [[[0] * N for _ in range(N)] for _ in range(M)]
# convenient : index 1부터
while True:
    time += 1
    for no in range(1, M+1):
        que = in_arr[no]
        if que:
            move(que, no)
    if remain == 0:
        print(time)
        break
    if time <= M: into_basecamp(*convenient[time])

