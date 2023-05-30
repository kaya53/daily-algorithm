# 230530 python 923ms => 2시간 ~ 2시간 30분 소요
# 유의할 점
# 1. 윷놀이 판에서 겹치는 번호 처리가 까다로웠다.
# - 25, 30, 35, 40은 겹치는 것인데, 42는 종료이기 때문에 겹친다고 표시하면 안됨

import sys

# sys.stdin = open('input.txt')


def backtrack(idx, score):
    global res

    if idx == 10:
        if res < score: res = score
        return

    for nnext in range(4):
        board_no, now_loc, now_num = horse[nnext]
        if now_num == 42: continue  # 이미 도착한 말
        next_loc = now_loc + order[idx]
        end = len(board[board_no])-1
        if next_loc > end: next_loc = end
        if board_no == 0:  # 다음 보드로 이동
            if next_loc == 5: board_no, next_loc = 1, 0
            elif next_loc == 10: board_no, next_loc = 2, 0
            elif next_loc == 15: board_no, next_loc = 3, 0
        # 25, 30, 35, 40는 공통; 공통 부분 처리
        next_num = board[board_no][next_loc]
        flag = False
        if next_num in common.keys():
            for com in common[next_num]:
                if com in horse:
                    flag = True
                    break
        if flag: continue
        # 말이 있는 칸은 건너뛴다
        if next_num != 42 and [board_no, next_loc, next_num] in horse: continue

        # 백트래킹 부분
        tmp = horse[nnext]
        horse[nnext] = [board_no, next_loc, next_num]
        if next_loc != end: score += next_num
        backtrack(idx+1, score)
        horse[nnext] = tmp
        if next_loc != end: score -= next_num


board = [
    list(range(0, 43, 2)),  # idx: 0 ~ 21
    [10, 13, 16, 19, 25, 30, 35, 40, 42],
    [20, 22, 24, 25, 30, 35, 40, 42],
    [30, 28, 27, 26, 25, 30, 35, 40, 42]
]
common = {
    25: [[1, 4, 25], [2, 3, 25], [3, 4, 25]],
    30: [[1, 5, 30], [2, 4, 30], [3, 5, 30]],
    35: [[1, 6, 35], [2, 5, 35], [3, 6, 35]],
    40: [[0, 20, 40], [1, 7, 40], [2, 6, 40], [4, 7, 40]]
}
# for _ in range(3):
order = list(map(int, input().split()))
horse = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

res = 0
backtrack(0, 0)
print(res)