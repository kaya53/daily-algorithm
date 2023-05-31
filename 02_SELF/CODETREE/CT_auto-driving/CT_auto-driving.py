# 230531 python 181ms => 1시간 ~ 1시간 30분 소요
# 유의할 점
# 1. 운행 중에 배터리가 닳는 경우를 고려해야 함
# 2. 태울 수 있는 승객이 여러 명일 때 정렬하기
# 3. 승객의 출발지, 도착지 자료구조
import sys

sys.stdin = open('input.txt')

from collections import deque


def to_passenger():
    global battery

    visited = [[0] * N for _ in range(N)]
    q = deque([(taxi_i, taxi_j)])
    visited[taxi_i][taxi_j] = 1
    cand = []
    flag = False
    dist = -1
    while q:
        dist += 1
        if dist > battery: return False  # 현재까지 이동량이 배터리 잔량보다 많을 때
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if departure[ci][cj]:
                flag = True
                cand.append((dist, ci, cj, departure[ci][cj]))

            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                # 인덱스 밖, 벽, 이미 지나온 곳
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] or visited[ni][nj]: continue
                q.append((ni, nj))
                visited[ni][nj] = 1
        if flag:
            cand.sort()
            # print(cand)
            return cand.pop(0)


def to_arrival(passenger_no):
    visited = [[0] * N for _ in range(N)]
    q = deque([(taxi_i, taxi_j)])
    visited[taxi_i][taxi_j] = 1

    dist = -1
    while q:
        dist += 1
        if dist > battery: return False  # 현재까지 이동량이 배터리 잔량보다 많을 때
        for _ in range(len(q)):
            ci, cj = q.popleft()
            if (ci, cj) == arrival[passenger_no]:
                # 여태까지 쓴 충전량 * 2
                return dist, arrival[passenger_no][0], arrival[passenger_no][1]
            for di, dj in delta:
                ni, nj = ci + di, cj + dj
                # 인덱스 밖, 벽, 이미 지나온 곳
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] or visited[ni][nj]: continue
                q.append((ni, nj))
                visited[ni][nj] = 1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(3):
N, M, battery = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
taxi_i, taxi_j = map(lambda x: int(x)-1, input().split())
departure = [[0] * N for _ in range(N)]
arrival = [0] * (M+1)
for m in range(1, M+1):
    sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
    departure[sr][sc] = m
    arrival[m] = (er, ec)

remain = M
while True:
    # 모든 승객 이동 완료
    if remain == 0:
        print(battery)
        break
    # 승객에게 이동
    res_passenger = to_passenger()
    if not res_passenger:
        print(-1)  # 배터리가 없어서 끝난 것
        break
    p_used, taxi_i, taxi_j, p_no = res_passenger
    departure[taxi_i][taxi_j] = 0  # 도착한 승객은 출발지에서 없애기
    battery -= p_used
    
    # 목적지로 이동
    res_arrival = to_arrival(p_no)
    if not res_arrival:
        print(-1)
        break
    a_used, taxi_i, taxi_j = res_arrival
    battery += a_used
    remain -= 1
