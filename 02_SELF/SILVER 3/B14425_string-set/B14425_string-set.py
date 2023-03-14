import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
strs = [input() for _ in range(n)]
check = [input() for _ in range(m)]

# check = set(check)

cnt = 0
for c in check:
    if c in strs:
        cnt += 1

print(cnt)