import sys

sys.stdin = open('input.txt')

# for _ in range(3):
# 행, 열 중 더 작은 수는 무조건 짝수
n, m, r = map(int, input().split())  # 행, 열, 회전 횟수
arr = [list(map(int, input().split())) for _ in range(n)]

# 오른쪽 - 아래쪽 - 왼쪽 - 위쪽
dir_ls = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# rot = ((n*2 + m*2) - 4) % 4
for _ in range(r): # r번 회전
    # 반시계 방향 회전
    for i in range(n//2):  # n: 5, m: 4일 때 ;; i: 0, 1
        si, sj = i, i+1  # 달팽이처럼 돌자-- 이렇게 하니까 시간 초과남
        k = 0
        tmp = arr[i][i+1]
        while True:
            if si == i and sj == i:
                arr[si][sj] = tmp
                break
            ni, nj = si + dir_ls[k][0], sj + dir_ls[k][1]
            if ni < i or ni >= n-i or nj < i or nj >= m-i:
                k = (k+1) % 4
                continue
            arr[si][sj] = arr[ni][nj]
            si, sj = ni, nj


for elem in arr:
    print(' '.join(map(str, elem)))