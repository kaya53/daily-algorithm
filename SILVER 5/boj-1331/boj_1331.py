import sys

sys.stdin = open('input.txt')


## 1차 제출 코드 -- 메모리 113mb, 시간 1초 16 (제한: 128mb, 시간 2초)
### pypy로 내니까 느린 거였음 ; 같은 코드를 python으로 돌리니까 40ms 나옴
# def str_to_int(arr):
#     # print(ord('A'), ord('F')) # 65 70
#     for i in range(36):
#         col = ord(arr[i][0]) - 65
#         row = int(arr[i][1]) - 1
#         arr[i] = (row, col)
#     return arr

#
# def not_knight(new_arr, chess):
#     for num in range(36):
#         i, j = new_arr[num]
#         if chess[i][j] == 1:  # 겹친다는 의미
#             return 'Invalid'
#         else:
#             chess[i][j] = 1  # 방문 표시
#
#             eight_side = [(i - 2, j + 1), (i - 1, j + 2), (i - 2, j - 1), (i - 1, j - 2), (i + 2, j + 1),
#                           (i + 1, j + 2), (i + 2, j - 1), (i + 1, j - 2)]
#             if num == 35: num = -1  # 마지막에서 첫번째로 가야하니까
#             x = new_arr[num+1]
#             if x not in eight_side:  # 다음 점이 8방향 안에 없으면
#                 return 'Invalid'  # 끝
#     return 'Valid'
#
#
# input = sys.stdin.readline
# arr = [input().rstrip() for _ in range(36)]  # 움직일 칸들
# chess = [[0]*6 for _ in range(6)]  # 빈 체스판
#
# new_arr = str_to_int(arr)  # 좌표로 바꾼 arr
#
# print(not_knight(new_arr, chess))  # 나이트투어 유효성 판별
        

### 다른 코드를 보니까
## 겹치면 안되는 건 -  set로
## 나이트 이동 범위인 지 확인은 abs로 서로 좌표값을 빼기
## 개천재 movegreen... 마지막에서 첫번째로 와야 하니까
# ci, cj = arr[i] / ni, nj = arr[i-1]이라고 놨을 때 첫 턴에서 마지막과 처음이 나이트 움직임으로 유효한 지 확인 가능
# 내 코드가 틀렸던 이유가 append((0,0))을 해줘서 그렇다
# 여기로 돌아온다는 게 아니라 주어진 칸 중 첫번째로 돌아온다는 의미
def str_to_int(arr):
    # print(ord('A'), ord('F')) # 65 70
    for i in range(36):
        col = ord(arr[i][0]) - 65
        row = int(arr[i][1]) - 1
        arr[i] = (row, col)
    return arr


def not_knight(arr):
    if len(set(arr)) != 36:  # 겹치는 게 있다면
        # print('set', end=' ')
        return 'Invalid'
    else:
        for i in range(35):
            # ci, cj = new_arr[i]
            # ni, nj = new_arr[i - 1]
            abs_col = abs(ord(arr[i][0]) - ord(arr[i-1][0]))
            abs_row = abs(int(arr[i][1]) - int(arr[i-1][1]))

            if (abs_row == 1 and abs_col == 2) or (abs_row == 2 and abs_col == 1):
                continue
            else:
                # print('abs', end=' ')
                return 'Invalid'

    return 'Valid'


for _ in range(5):
    input = sys.stdin.readline
    arr = [input().rstrip() for _ in range(36)]  # 움직일 칸들
    # chess = [[0]*6 for _ in range(6)]  # 빈 체스판

    # new_arr = str_to_int(arr)  # 좌표로 바꾼 arr
    # new_arr.append((0,0))  # 마지막에 처음으로 돌아와야 하니까 붙임

    print(not_knight(arr))





