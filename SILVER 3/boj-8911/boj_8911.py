# import sys
#
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for _ in range(T):
#     route = input()
#     # print(route)
#
#     dir = [0, 1, 2, 3]  # 각 인덱스는 북동남서를 가리킴
#     now_dir = idx_d = 0  # now_dir: 현재 달팽이의 방향, idx_d: dir을 순회하는 인덱스
#     # 북동남서 순
#     move_ls = [[(1, 0), (-1, 0)],
#                [(0, 1), (0, -1)],
#                [(-1, 0), (1, 0)],
#                [(0, -1), (0, 1)]]
#     snail = [(0, 0)]
#     snail_i, snail_j = 0, 0  # 달팽이의 현 위치
#     for elem in route:
#         if elem == 'F':
#             snail_i += move_ls[now_dir][0][0]
#             snail_j += move_ls[now_dir][0][1]
#             snail.append((snail_i, snail_j))
#
#         elif elem == 'B':
#             snail_i += move_ls[now_dir][1][0]
#             snail_j += move_ls[now_dir][1][1]
#             snail.append((snail_i, snail_j))
#
#         elif elem == 'L':
#             idx_d -= 1
#
#         elif elem == 'R':
#             idx_d -= 3
#         now_dir = dir[idx_d]
#         idx_d = now_dir  # 이걸 해줘야 계속 -로 안감
#
#     res = list(zip(*snail))
#     res_row = sorted(res[0])
#     res_col = sorted(res[1])
#
#     print((res_row[-1] - res_row[0]) * (res_col[-1] - res_col[0]))
#
#
#
# ## 10배 정도 빠른 코드들을 보니까(메모리도 10배 정도 차이남)
# ## % 연산자를 이용해 방향 전환을 구현함
#
#

import sys

sys.stdin = open('input.txt')

T = int(input())
# 아래 배열은 모든 테케에 대해서 동일하게 쓰이니까 밖으로 뺐음
# 북-동-남-서/상-우-하-좌
# df = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# db = [(-1, 0), (0, -1), (1, 0), (0, 1)]
di = [1, 0, -1, 0]
dj = [0, 1, 0 , -1]


def turtle(route, now_d, ci, cj):
    # 방향 전환
    res_i, res_j = [0], [0]
    for elem in route:
        if elem == 'L':
            now_d = (now_d + 3) % 4
        elif elem == 'R':
            now_d = (now_d + 1) % 4
        elif elem == 'F':
            ci += di[now_d]
            cj += dj[now_d]
            res_i.append(ci)
            res_j.append(cj)
        else:
            ci += di[(now_d+2) % 4]
            cj += dj[(now_d+2) % 4]
            res_i.append(ci)
            res_j.append(cj)

    height = max(res_i) - min(res_i)
    width = max(res_j) - min(res_j)
    return width*height


for _ in range(T):
    route = input()
    ci, cj, now_d = 0, 0, 0  # 맨 처음 달팽이의 위치, 방향

    print(turtle(route, now_d, ci, cj))

