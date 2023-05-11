# 시간초과 해결
# 1. if i-1 >= 0 이런 식으로 작성했던 것을 if i > 0으로 바꿈
# 2. sys.stdin.readline으로 input을 받음

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0] * N for _ in range(N)]

# 구간 합 구하기
for i in range(N):
    for j in range(N):
        a = b = c = 0
        d = arr[i][j]
        if i > 0 and j > 0:
            a = sum_arr[i-1][j-1]
        if i > 0:
            b = sum_arr[i-1][j]
        if j > 0:
            c = sum_arr[i][j-1]
        sum_arr[i][j] = b+c+d-a

for _ in range(M):
    si, sj, ei, ej = map(lambda x: int(x)-1, input().split())
    std = sum_arr[ei][ej]
    area1 = (sum_arr[si-1][ej] if si > 0 else 0)
    area2 = (sum_arr[ei][sj-1] if sj > 0 else 0)
    doubled = (sum_arr[si-1][sj-1] if si > 0 and sj > 0 else 0)
    print(std-area1-area2+doubled)