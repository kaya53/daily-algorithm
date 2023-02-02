import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

paper = [[0] * 100 for _ in range(100)]

for elem in arr:
    ci = 100 - elem[1] - 1
    cj = elem[0] - 1
    for i in range(ci, ci-10, -1):
        for j in range(cj, cj+10):
            if paper[i][j] == 0:
                paper[i][j] = 1

ssum = 0
for ls in paper:
    ssum += sum(ls)

print(ssum)