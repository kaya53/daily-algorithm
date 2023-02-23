import sys

sys.stdin = open('input.txt')


def comb(tdy, cost):
    global mmax

    if tdy == n:
        if mmax < cost:
            mmax = cost
        return
    t = arr[tdy][0]
    p = arr[tdy][1]
    # cost += arr[tdy][1]
    if t + tdy <= n:
        comb(tdy+t, cost+p)
    comb(tdy+1, cost)

# for _ in range(3):
n = int(input())  # 일하는 시간
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
mmax = 0
for i in range(n):
    comb(i, 0)
print(mmax)