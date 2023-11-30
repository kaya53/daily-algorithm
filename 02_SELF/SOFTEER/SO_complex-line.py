# 틀린 이유
# 1. input 받을 때 moving이 3차원이 되게 하지 않음
# 2. dp 로직 오류
# - j번째 라인의 i번째 작업장까지의 최소 시간 = min(그대로 온 것, 다른 라인 갔다가 온 것)
# - line[i+1][j]: 같은 라인의 다른 작업장
import sys


K, N = map(int, input().split())  # 라인 수, 작업장
line = []  # 라인마다 j번째 작업장의 작업 소요 시간
moving = [[[0] * K for _ in range(K)] for _ in range(N)]  # j번째 작업장에서 i번째 라인에서 다른 라인으로 옮기는 데 소요되는 시간
# 이동 시간이니까 K-1번째는 없음
for t in range(N - 1):
    inp = list(map(int, input().split()))
    line.append(inp[:K])

    c = 0
    for z in range(K):
        for p in range(K):
            if p == z: continue  # 같은라인, 이동 시간 0
            moving[t][z][p] = inp[K + c]
            c += 1

line.append(list(map(int, input().split())))

for i in range(N - 1):  # i번째 작업장
    for j in range(K):  # j번째 라인
        v = line[i][j]  # j번째 라인의 i번째 작업장에서 소요되는 최소 시간
        for a in range(K):  # 다른 라인
            if j == a: continue
            v = min(v, line[i][a] + moving[i][a][j])  # 기존 최소 시간, 다른 라인 거쳐서 현재 라인으로 오는 시간
        line[i+1][j] += v  # 같은 라인의 다음 작업장
print(min(line[-1]))