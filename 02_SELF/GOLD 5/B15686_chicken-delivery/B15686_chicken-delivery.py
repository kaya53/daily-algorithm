import sys

sys.stdin = open('input.txt')

from collections import deque

def comb(cnt, si, arr):
    if cnt == M:
        chicken_comb.append(arr)
        return
    for i in range(si, whole_cnt):
        comb(cnt+1, i+1, arr+[chicken[i]])


# for _ in range(4):
N, M = map(int, input().split())  # 도시 크기, 유지해야 할 치킨집 수
zeros = [[0] * (N+2)]
city = zeros + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + zeros

# 1. 지금 도시에 있는 치킨집 구하기
chicken = deque()
house = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))
# print(chicken)  # deque([(1, 2), (4, 1), (5, 1), (5, 2), (5, 5)])

# 2. 조합 구하기
whole_cnt = len(chicken)
chicken_comb = deque()  # 각 원소는 치킨집 좌표 모음
comb(0, 0, [])
# print(chicken_comb)

# 3. 이 조합 결과를 가지고 최소 거리를 구하기
res_dist = 10**7  # 이 부분을 100으로 해놔서 틀렸었음 힣
while chicken_comb:
    c_combs = chicken_comb.popleft()
    # print(elem)  # [(1, 2), (4, 1)]

    # 이 조합의 최소 치킨 거리 ; 새로운 조합이 들어올 때 마다 갱신
    city_dist = 0
    for hi, hj in house:  # 모든 집에 대해서
        house_dist = 100  # 치킨 거리: 한 집에서 가능한 최소 거리
        for ci, cj in c_combs:  # 가능한 집들을 살펴 본다
            # print('ci, cj= ', ci, cj)
            dist = abs(hi-ci) + abs(hj-cj)
            if house_dist > dist:  # 최솟값 갱신
                house_dist = dist
        # 한 집 순회 끝
        # print(house_dist)
        city_dist += house_dist

    # 모든 집에 대해서 다 순회하면
    if res_dist > city_dist:
        res_dist = city_dist
print(res_dist)