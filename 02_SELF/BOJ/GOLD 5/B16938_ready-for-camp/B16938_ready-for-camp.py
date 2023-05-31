# 230531 python 128ms => 30분 소요
import sys

sys.stdin = open('input.txt')


def comb(idx, ci):
    global res

    if idx == num:
        if (L <= sum(choice) <= R) and (max(choice) - min(choice) >= X):
            res += 1
        return

    for ni in range(ci, N):
        choice[idx] = arr[ni]
        comb(idx+1, ni + 1)
        choice[idx] = 0


N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))

res = 0
for num in range(2, N+1):
    choice = [0] * num
    comb(0, 0)

print(res)