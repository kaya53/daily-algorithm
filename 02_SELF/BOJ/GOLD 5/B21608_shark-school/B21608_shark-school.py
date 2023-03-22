import sys

sys.stdin = open('input.txt')


def seat(a, b, c, d, e) :
    res_ls = []
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                l_tmp, z_tmp = 0, 0  # 좋아하는 학생 수와 인접한 0의 개수를 세줌
                for di, dj in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                    if arr[ni][nj] in [b, c, d, e]:  # 사방에 좋아하는 학생이 있는 경우
                        l_tmp += 1
                    if not arr[ni][nj]: z_tmp += 1  # 주변이 0인 경우
                res_ls.append((l_tmp, z_tmp, i, j))
    sort_res = sorted(res_ls, key=lambda x: (-x[0], -x[1], x[2], x[3]))

    for l, z, ii, jj in sort_res:
        if not arr[ii][jj]:
            arr[ii][jj] = a
            break


def check():
    global res
    for i in range(n):
        for j in range(n):
            now = arr[i][j]
            cnt = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                if arr[ni][nj] in pref[now]:
                    cnt += 1
            if cnt == 1: res += 1
            elif cnt == 2: res += 10
            elif cnt == 3: res += 100
            elif cnt == 4: res += 1000


# for _ in range(2):
n = int(input())
NUM = n**2
arr = [[0] * n for _ in range(n)]
pref = {}

for _ in range(NUM):
    # 상어 학생 입장
    a, b, c, d, e = map(int, input().split())
    pref[a] = [b, c, d, e]
    seat(a, b, c, d, e)

# 만족도 체크
res = 0
check()
print(res)