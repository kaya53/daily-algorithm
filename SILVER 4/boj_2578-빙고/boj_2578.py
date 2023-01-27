import sys

sys.stdin = open('input.txt')

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]

# mc가 부른 숫자의 빙고판 위치
mc_num = [[] for _ in range(5)]
cnt = 0
while cnt < 5:
    nums = map(int, sys.stdin.readline().rstrip().split())
    for num in nums:
        for i in range(5):
            for j in range(5):
                if num == arr[i][j]:
                    mc_num[cnt].append((i, j))
    cnt += 1


# 빙고 판별
rows = [[] for _ in range(5)]
cols = [[] for _ in range(5)]
ssums = []
ssame = []
ccnt = 0

for k in range(5):
    for z in range(5):
        row, col = mc_num[k][z]
        rows[row].append((row, col))
        cols[col].append((row, col))
        if len(rows[row]) == 5:
            ccnt += 1
        if len(cols[col]) == 5:
            ccnt += 1

        if row + col == 4:
            ssums.append((row, col))
            if len(ssums) == 5:
                ccnt += 1
        if row == col:
            ssame.append((row, col))
            if len(ssame) == 5:
                ccnt += 1
        if ccnt == 3:
            break
    if ccnt == 3:
        print(5*k + (z+1))
        break
