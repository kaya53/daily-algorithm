import sys

sys.stdin = open('input.txt')

N = int(input())  # 색종이수
arr = [tuple(map(int, input().split())) for _ in range(N)]

paper = [[0] * 100 for _ in range(100)]
length = [[], []]
for elem in arr:
    ci = 100 - elem[1] - 1
    cj = elem[0] - 1
    length[1].append(ci)
    length[0].append(cj)
    for i in range(ci, ci-10, -1):
        for j in range(cj, cj+10):
            if not paper[i][j]:
                paper[i][j] = 1

## 내부 비우기
# min_i, max_i = min(elem[1]), max(elem[1])
# min_j, max_j = min(elem[0]), max(elem[0])
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:  # 값이 1일 때만 사방 탐색
            for k in range(4):  # 사방 탐색
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < 100 and 0 <= nj < 100:  # 인덱스 내부이고
                    if paper[ni][nj] == 0:  # 주변에 0이 있으면
                        cnt += 1
                else:  # 인덱스 외부 -> 모서리이므로 1을 더해준다.
                    cnt += 1

print(cnt)

paper.count()