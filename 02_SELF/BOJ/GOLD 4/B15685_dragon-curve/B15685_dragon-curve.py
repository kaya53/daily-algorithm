import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def draw_curve(si, sj, d, g):
    # k-1세대의 방향 배열 + 뒤집어서 그 반대로 배열 => k세대 커브
    ci, cj = si+delta[d][0], sj+delta[d][1]
    arr[si][sj] = arr[ci][cj] = 1  # 0세대
    now_g = 0  # 현재 세대
    now_dir = [d]
    while now_g < g:
        for nd in now_dir[::-1]:
            ci += delta[(nd+1) % 4][0]
            cj += delta[(nd+1) % 4][1]
            arr[ci][cj] = 1
            # print(ci, cj)
            now_dir.append((nd+1)%4)
        now_g += 1  # 세대 하나 늘리기
    # print(now_dir)
    # return now_dir


delta = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 0123 => 1230 (d+1)%4
# for _ in range(4):
n = int(input())
arr = [[0] * 101 for _ in range(101)]
infos = [list(map(int, input().split())) for _ in range(n)]

# dir_ls = []
for sj, si, d, g in infos: # i, j 뒤집기
    draw_curve(si, sj, d, g)

# 크기가 1*1인 정사각형의 개수 찾기
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            if arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1]:
                cnt += 1
print(cnt)
