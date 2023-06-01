# 230601 python 99ms => 1시간 30분 정도 소요
# 영양제를 옮기고 바로 나무를 키워줘야 답이 맞게 나온다
# - 만약에 높이가 0인 나무가 영양제를 먹었다고 하면
# - grow_up에서 한 번에 처리해주면, 이 대각선에 있는 리브로수는 높이가 1 미만이라고 판단해 높이를 높이지 않을 것
# - 따라서 grow_up을 하기 전에 미리 모든 나무 높이를 올려놔야 답이 맞음
import sys

sys.stdin = open('input.txt')


def move_nutrition(cd, cnt):
    for idx, nu in enumerate(nutri):
        ci, cj = nu
        ni = (ci + delta[cd][0]*cnt) % N
        nj = (cj + delta[cd][1]*cnt) % N
        nutri[idx] = (ni, nj)
        arr[ni][nj] += 1  # 여기에 붙이면 답이 나오고 grow_up에 붙이면 답이 다르게 나옴


def grow_up():
    # 1씩 증가
    # print(nutri)
    for ci, cj in nutri:
        for di, dj in [(-1, 1), (-1, -1), (1, 1), (1, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if arr[ni][nj]: arr[ci][cj] += 1
    # print('grow up --------------')
    # for a in arr:
    #     print(a)
    # print()


def cut_and_nutri():
    # print(nutri)
    new_nutri = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in nutri:
                arr[i][j] -= 2
                new_nutri.append((i, j))
    # print('after cut --------------')
    # for a in arr:
    #     print(a)
    # print()
    return new_nutri


delta = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
# delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [() for _ in range(M)]
for m in range(M):
    d, p = map(int, input().split())
    move[m] = (d-1, p)
nutri = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

for year in range(M):
    # print(year, move[year], '---------------------')
    # print(nutri)
    move_nutrition(*move[year])
    grow_up()
    nutri = cut_and_nutri()
    # print(nutri)


res = 0
for a in arr:
    # print(a)
    res += sum(a)
print(res)