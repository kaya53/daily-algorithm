import sys

sys.stdin = open('input.txt')

def solution():
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    d = [0] * n

    if len(stairs) <= 2:
        return sum(stairs)
    else:
        d[0] = stairs[0]
        d[1] = stairs[0] + stairs[1]

        for i in range(2, n):
            # 그 전 칸에서 1칸으로 올라왔을 때 vs. 두칸으로 올라왔을 때
            d[i] = max(d[i-3]+stairs[i-1]+stairs[i], d[i-2]+stairs[i])
    return d[-1]


print(solution())
