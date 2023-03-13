import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def move_color(ni, nj, d, horse_no, clr, horse_info):
    # horse_info: k번 말이 현재 위치해 있는 곳에 말이 얼마나 쌓여 있는 지
    if not clr:  # 흰색
        print('wh', horse_info, horse_no)
    elif clr == 1:  # 빨간색
        print('red', horse_info, horse_no)
    elif clr == 2:  # 파란색
        if chess[ni][nj] != 2:  # 반대로 돌았는데 파란색이 아닌 경우
            infos[horse_no] = [ni, nj, d]  # 기존 말의 정보 수정; 좌표, 방향 수정
            # 내 말 하나만 이동
            nnext = horse_info[ni][nj]
            if nnext:
                nnext[horse_no] = len(nnext)
            else:
                horse_info[ni][nj] = {horse_no: 0}  # 말 번호, 순서


def move_horses():
    for i in range(1, k+1):  # 1번부터 k까지 차례로 이동
        hi, hj, hd = infos[i]  # 현재 말의 좌표와 방향
        now_horse = horse_info[hi][hj]  # 현재 말 위에 얼마나 얹혀져 있는 지
        if now_horse and len(now_horse) > 1:
            tmp = [0] * len(now_horse)
            tmp[0] = i
            std = now_horse[i]  # 현 좌표에서 지금 말의 순서
            for z in range(i, k+1):
                if now_horse[z] < std: continue
                tmp[now_horse[z]-std] = i
            now_horse = tmp
        ni, nj = hi + delta[hd][0], hj + delta[hd][1]
        # 인덱스 밖 or 파란색인 경우
        if ni < 0 or ni >= n or nj < 0 or nj >= n or chess[ni][nj] == 2:
            oppo_d = (5 - hd) % 4
            ni, nj = hi + delta[oppo_d][0], hj + delta[oppo_d][1]
            move_color(ni, nj, oppo_d, i, 2, 0)
            continue

        if chess[ni][nj] == 0 or chess[ni][nj] == 1:
            move_color(ni, nj, hd, i, chess[ni][nj], now_horse)  # 인덱스 안일 때 흰, 빨, 파를 만났을 때


# input
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오-왼-위-아래 순
# oppo = {0: 1, 1: 0}
n, k = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(n)]
horse_info = [[0] * n for _ in range(n)]
infos = {}
for x in range(1, k+1):
    r, c, d = map(int, input().split())
    infos[x] = [r-1, c-1, d-1]

# print(infos)  # {1: [1, 0, 0], 2: [2, 1, 2], 3: [1, 1, 0], 4: [3, 0, 1]}

turn = 0
while True:
    turn += 1
    move_horses()
    break
