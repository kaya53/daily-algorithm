# 230524 python 1407ms -- 40-50분
# k 라운드 시뮬레이션
# 주어진 바이러스 정보를 딕셔너리에 넣을 것인가, 2차원 리스트에 저장할 것인가
import sys

sys.stdin = open('input.txt')


def eat_nutrition():
    dead = []
    for i in range(N):
        for j in range(N):
            if virus[i][j]:
                virus[i][j].sort()
                while virus[i][j]:
                    for _ in range(len(virus[i][j])):
                        age = virus[i][j].pop(0)
                        if arr[i][j] < age:
                            dead.append((i, j, int(age/2)))
                            continue
                        arr[i][j] -= age
                        virus[i][j].append(age+1)
                    break
    return dead


def dead_to_nutrition(dead):
    for dei, dej, plus in dead:
        arr[dei][dej] += plus


def spread_virus():
    for ci in range(N):
        for cj in range(N):
            if virus[ci][cj]:
                for age in virus[ci][cj]:
                    if not age % 5:
                        for di, dj in delta:
                            ni, nj = ci + di, cj + dj
                            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                            virus[ni][nj].append(1)


def plus_nutrition():
    for ci in range(N):
        for cj in range(N):
            arr[ci][cj] += nutrition[ci][cj]


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, -1), (1, 1)]
N, M, K = map(int, input().split())
arr = [[5]*N for _ in range(N)]
nutrition = [list(map(int, input().split())) for _ in range(N)]

virus = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    i, j, a = map(int, input().split())
    virus[i-1][j-1].append(a)

for _ in range(K):
    dead_virus = eat_nutrition()
    # print(dead_virus)
    if dead_virus: dead_to_nutrition(dead_virus)
    spread_virus()
    plus_nutrition()

# output
res = 0
for vv in virus:
    for v in vv:
        if v: res += len(v)
print(res)
