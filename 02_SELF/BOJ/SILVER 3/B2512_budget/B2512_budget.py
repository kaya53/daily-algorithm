import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def solve():
    global start, end, mmax

    while True:
        ssum = 0
        mid = (start + end) // 2
        if start == mid or end == mid:
            return mid

        for cost in infos:
            if cost < mid:
                ssum += cost
            else:
                ssum += mid
        if ssum > max_budget:
            end = mid
        else:
            start = mid
            if mmax < ssum:
                mmax = ssum


# for _ in range(3):
n = int(input())
infos = list(map(int, input().split()))
max_budget = int(input())
infos.sort()
start, end = max_budget // n, infos[-1]
mmax = 0
if sum(infos) <= max_budget:
    print(infos[-1])
else:
    print(solve())



