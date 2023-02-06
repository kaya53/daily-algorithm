import sys
import copy

sys.stdin = open('input.txt')

# 아래 -> 위: 63700kb / 263ms
di, dj = [0, 0, -1], [-1, 1, 0]  # 왼 오 위 순
def find_start(si, sj):
    while si >= 0:
        for k in range(3):
            ni, nj = si+di[k], sj+dj[k]
            if (0 <= ni < 100) and (0 <= nj < 100) and arr[ni][nj]:
                if ni == 0:
                    return nj
                arr[ni][nj] = 0
                si, sj = ni, nj



# 위 -> 아래 : 66604kb / 344ms
# di, dj = [0, 0, 1], [-1, 1, 0]  # 왼 오 아래 순
# def find_start():
#     for j in range(100):
#         if arr[0][j] == 1:
#             copy_arr = copy.deepcopy(arr)
#             si, sj = 0, j
#             ci, cj = si, sj
#             while ci <= 99:
#                 if ci == 99 and copy_arr[ci][cj] != 2:
#                     break
#                 for k in range(3):
#                     ni, nj = ci+di[k], cj+dj[k]
#                     if (0 <= ni < 100) and (0 <= nj < 100):
#                         if copy_arr[ni][nj] == 1:
#                             copy_arr[ni][nj] = 0  # 일종의 방문 표시
#                             ci, cj = ni, nj  # 이동
#                             break  # 한번 이동했으면 다음으로
#                         elif copy_arr[ni][nj] == 2:
#                             return sj


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                res = find_start(i, j)

    # res = find_start()
    print(f'#{tc} {res}')

