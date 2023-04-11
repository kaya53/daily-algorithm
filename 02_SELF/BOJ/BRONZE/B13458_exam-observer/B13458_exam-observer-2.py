import sys, math

input = sys.stdin.readline

N = int(input())
locs = list(map(int, input().split()))
B, C = map(int, input().split())

res = N
for i in range(N):
    all = locs[i] - B
    if all > 0:
        res += math.ceil(all / C)
print(res)