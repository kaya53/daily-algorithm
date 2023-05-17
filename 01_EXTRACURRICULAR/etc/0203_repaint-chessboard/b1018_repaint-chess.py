import sys
import copy

sys.stdin = open('input.txt')


# 상 하 좌 우
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
# def cnt_painting_01(si, sj):  # 잘라낸 8*8 보드에서 필요한 칸 칠하기
#     copy_arr = copy.deepcopy(arr)
#     paint_cnt = 0
#     for i in range(si, si+8):
#         for j in range(sj, sj+8):
#             # 새로운 칸을 볼 때 cnt들 갱신
#             # 탐색 가능한 인덱스 수 셈, 나와 같은 칸이 몇 개인지 셈, 다시 칠해야 하는 칸 수 셈
#             idx_cnt = same_cnt = 0
#             for k in range(4):
#                 ni, nj = i + di[k], j + dj[k]
#                 if (si <= ni < si+8) and (sj <= nj < sj+8):
#                     idx_cnt += 1
#                     if copy_arr[i][j] == copy_arr[ni][nj]:
#                         same_cnt += 1
#             # 사방 탐색 완료
#             # 탐색 가능한 인덱스 내 칸이 모두 내 것과 같으면
#             if idx_cnt == same_cnt:
#                 paint_cnt += 1  # 칠해주기
#                 if copy_arr[i][j] == 'B':
#                     copy_arr[i][j] = 'W'
#                 else:
#                     copy_arr[i][j] = 'B'
#     return paint_cnt


def cnt_painting(si, sj):  # 잘라낸 8*8 보드에서 필요한 칸 칠하기; 위 코드보다 쓴 변수가 적은 방법
    copy_arr = copy.deepcopy(arr)
    paint_cnt = 0
    for i in range(si, si+8):
        for j in range(sj, sj+8):
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if (si <= ni < si+8) and (sj <= nj < sj+8):
                    if copy_arr[ni][nj] == copy_arr[i][j]:  # 주위가 나랑 다 달라야 하니까 같으면 바꾸기
                        paint_cnt += 1
                        # 토글링
                        if copy_arr[i][j] == 'B':
                            copy_arr[ni][nj] = 'W'
                        else:
                            copy_arr[ni][nj] = 'B'
    return paint_cnt


input = sys.stdin.readline

for _ in range(7):
    N, M = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]
    # print(arr)

    min_cnt = 32  # 큰 값; 만약 모두 바꿔야 한다면 32번 바꿔야 하므로
    for i in range(N-8+1):
        si = i
        for j in range(M-8+1):
            sj = j
            res_cnt = cnt_painting(si, sj)
            if res_cnt > 32:  # 모두 B거나 W일때 최대로 바꾸는 게 32개; 이것보다 크면 최소가 될 수 없음
                res_cnt = 64 - res_cnt  # 모두 바꾸는 경우 64번이니까
            if min_cnt > res_cnt:
                min_cnt = res_cnt
    print(min_cnt)