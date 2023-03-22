import sys

sys.stdin = open('input.txt')

import heapq
from collections import deque


def find_customer(si, sj):
    global oil, ti, tj

    visited = [[0] * n for _ in range(n)]  # 출발점 -> 도착점까지 visited
    visited[si][sj] = -1
    # 현재 택시가 위치한 점에서 승객까지의 거리
    res = []
    min_dist = int(1e9)
    q = deque()
    q.append((0, si, sj))  # 승객까지 최단 경로, 현재 택시 위치
    while q:
        dist, ci, cj = q.popleft()
        # 여기서 현재 연료 잔량 < dist이면 return -1 하도록 하기
        if min_dist < dist: break

        if arr[ci][cj] and arr[ci][cj] != 1:  # 1, 0 둘다 아니면 도착지임
            min_dist = dist
            res.append((ci, cj, arr[ci][cj][0]))  # 도착 좌표, 승객 번호
            if oil <= min_dist:
                return False  # 여기서는 같아도 안됨; 같으면 도착지까지 갈 연료가 없으니까

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 1: continue
            if visited[ni][nj]: continue
            visited[ni][nj] = dist + 1
            q.append((dist+1, ni, nj))
    
    # 여기서 연료 잔량 계산하기
    if res:
        oil -= min_dist
        res.sort(key=lambda x: (x[0], x[1]))  # 승객 번호, 도착 좌표; 이 부분 소트 키를 잘못 잡아서 틀렸었음
        # if len(res) > 1: print(res)
        arr[res[0][0]][res[0][1]] = 0
        return res[0]
    return False  # 어떤 승객에게도 갈 수 없음


def goto_arrival(si, sj, cus_no):  # 승객의 위치, 승객 번호
    global oil, ti, tj

    visited = [[0] * n for _ in range(n)]  # 출발점 -> 도착점까지 visited
    visited[si][sj] = -1
    ei, ej = customers[cus_no-1][2:]
    q = deque()
    q.append((0, si, sj))
    while q:
        dist, ci, cj = q.popleft()
        if oil < dist: return False

        if ci == ei and cj == ej:
            ti, tj = ei, ej
            # 여기서 oil 늘려주기
            # tot_used = used_oil + dist  # 출발지 ~ 승객 + 승객 ~ 도착지
            oil += dist   # 승객 ~ 도착지까지 소요 거리 빼주고, 총 합*2 해주기
            return True

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 1: continue
            if visited[ni][nj]: continue
            visited[ni][nj] = dist + 1
            q.append((dist + 1, ni, nj))


# for _ in range(13):
n, m, oil = map(int, input().split())  # 격자 크기, 승객 수, 초기 연료의 양
arr = [list(map(int, input().split())) for _ in range(n)]
ti, tj = map(int, input().split())  # 운행 시작점
customers = [[] for _ in range(m)]  # i+1번 승객의 출발 좌표, 도착 좌표
ti -= 1
tj -= 1

for x in range(m):
    inp = map(int, input().split())
    customers[x] = list(map(lambda x: x-1, inp))

# arr 출발지 좌표에 승객 번호와 도착 좌표 등록해두기; 승객의 출발지는 서로 다름; 출발지 == 도착지인 경우도 없음
for idx, cus in enumerate(customers, start=1):
    arr[cus[0]][cus[1]] = (idx, cus[2], cus[3])

ans = 0
# 출발점에서 승객까지 거리 구하기
for _ in range(m):
    # used_oil = 0  # 한번 도착할 때마다 충전되므로 여기서 초기화
    res1 = find_customer(ti, tj)  # 리턴값: 가장 가까운 승객의 위치, 승객 번호
    if not res1:
        ans = -1
        break
    si, sj, cus_no = res1
    # print(si, sj, res1)

    if not goto_arrival(si, sj, cus_no):  # 승객 번호로 해당 승객의 도착점 찾기
        ans = -1
        break
    ans = oil

print(ans)