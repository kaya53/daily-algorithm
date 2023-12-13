# 소요시간 40분 pypy 872ms
import sys

sys.stdin = open('input.txt')


def solution(height):
    inventory = B
    time = 0
    for i in range(N):
        for j in range(M):
            v = height - arr[i][j]
            if v > 0:  # 쌓기 가능
                if inventory >= v:
                    inventory -= v
                    time += v
                else:  # 쌓기만 되는 데 인벤 없는 상태
                    return -1
            else:  # 제거 가능
                v *= -1
                inventory += v
                time += 2*v
    return time


# for _ in range(3):
N, M, B = map(int, input().split())
arr = [[] for _ in range(N)]
minB = 257
maxB = 0
for z in range(N):
    inp = list(map(int, input().split()))
    arr[z] = inp
    minB = min(minB, min(inp))
    maxB = max(maxB, max(inp))

res_time, res_height = int(1e9), 0
for h in range(minB, maxB+1):
    t = solution(h)
    if t == -1: continue
    if res_time > t:
        res_time = t
        res_height = h
    elif res_time == t and res_height < h:
        res_height = h
print(res_time, res_height)