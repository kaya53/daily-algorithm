# 소요시간 1시간 반 python 2156ms pypy 400ms
# 틀린 이유
# 1. 열 우선 연산을 안함
# - 그 전 열에서의 연산값이 그 다음 열로 옮겨가는 형태이기 때문에 열 우선 연산을 해야 함
# 2. 나머지 연산을 제대로 안해줌
# - (a % N + b % N) % N = (a+b) % N
# - 이 문제에서 (a+b) % N 을 구해줘야 하니까 마지막에도 % MOD를 붙여야함
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

N, M = map(int, input().rstrip().split())
K = int(input())
hole = set()
for _ in range(K):
    a, b = map(lambda x: int(x)-1, input().rstrip().split())
    hole.add((a, b))
MOD = (10**9) + 7
hc = [[0] * M for _ in range(N)]
hc[0][0] = 1

# 홀짝
deltas = [[(1, -1), (0, -1), (-1, 0)], [(0, -1), (-1, -1), (-1, 0)]]
for j in range(M):
    for i in range(N):
        if (i, j) == (0, 0) or (i, j) in hole: continue
        delta = deltas[1]
        if j % 2: delta = deltas[0]

        for di, dj in delta:
            bi, bj = i+di, j+dj
            if bi < 0 or bi >= N or bj < 0 or bj >= M: continue
            hc[i][j] += hc[bi][bj] % MOD


print(hc[-1][-1] % MOD)  # 여기에도 MOD로 나머지 연산 해줘야 함