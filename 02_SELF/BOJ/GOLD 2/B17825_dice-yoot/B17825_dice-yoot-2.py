import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def move(loc, dice):  # 이동할 말 번호, 이동 전 말 위치, 이동할 칸 수
    step = 0
    # 이동하다가 25를 만나면
    while step < dice:
        loc += 1
        step += 1
        if new_board[loc] == 42:  # 말 이동 끝
            return loc
        if new_board[loc] == 25:
            loc = 36
    if loc == 5: loc = 22
    elif loc == 10: loc = 27
    elif loc == 15: loc = 31

    return loc


def backtrack(idx, score):
    global mmax
    if idx == 10:
        if mmax < score:
            mmax = score
        return
    for i in range(4):  # 다음 갈 말 정하기
        now = horses[i]
        if new_board[now] == 42: continue  # 도착점 도착
        new_loc = move(now, dices[idx])
        if new_board[new_loc] != 42:
            if new_loc in horses or same_dict.get(new_loc, -1) in horses: continue
        horses[i] = new_loc
        if new_board[horses[i]] == 42: backtrack(idx + 1, score)
        else: backtrack(idx+1, score+new_board[horses[i]])
        horses[i] = now


# 1차원 배열로 펴기
board_std = [i for i in range(0, 43, 2)]  # 0~ 21
board_10 = [10, 13, 16, 19, 25]  # 22 ~ 26
board_20 = [20, 22, 24, 25]  # 27 ~ 30
board_30 = [30, 28, 27, 26, 25]  # 31 ~ 35
board_25 = [25, 30, 35, 40, 42]  # 36 ~ 40
new_board = board_std + board_10 + board_20 + board_30 + board_25
same_dict = {
    5: 22,
    22: 5,
    10: 27,
    27: 10,
    15: 31,
    31: 15,
    20: 39,
    39: 20
}
# for _ in range(4):
dices = list(map(int, input().rstrip().split()))
horses = [0, 0, 0, 0]  # 말들의 현 위치
mmax = 0
backtrack(0, 0)
print(mmax)
