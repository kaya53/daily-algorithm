import sys

sys.stdin = open('input.txt')


from collections import deque

n, m, oil = map(int, input().split())  # 격자 크기, 승객 수, 초기 연료의 양
arr = [list(map(int, input().split())) for _ in range(n)]
si, sj = map(int, input().split())  # 운행 시작점
customers = [[] for _ in range(m)]  # i+1번 승객의 출발 좌표, 도착 좌표
si -= 1
sj -= 1

for x in range(m):
    inp = map(int, input().split())
    customers[x] = list(map(lambda x: x-1, inp))


# 출발점에서 승객까지 거리 구하기
visited = [[0] * n for _ in range(n)]
# 현재 택시가 위치한 점에서 승객까지의 거리
res = []
for cus in customers:
    q = deque()
    q.append((0, si, sj))  # 승객까지 최단 경로, 현재 택시 위치
    ssi, ssj = cus[:2]  # 승객의 출발점

    while q:
        dist, ci, cj = q.popleft()
        if ci == ssi and cj == ssj:
            res.append((dist, ci, cj))
            break

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 1: continue
            q.append((dist+1, ci, cj))
