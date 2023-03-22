import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def move_color(ni, nj, d, horse_no, clr, now_horse):
    # horse_info: k번 말이 현재 위치해 있는 곳에 말이 얼마나 쌓여 있는 지; 리스트
    if not clr:  # 흰색
        # print('wh', horse_info, horse_no)
        horse_info[ni][nj] += now_horse  # 말 위에 얹기
    elif clr == 1:  # 빨간색
        # print('red', horse_info, horse_no)
        horse_info[ni][nj] += now_horse  # 말 위에 얹기
    elif clr == 2:  # 파란색
        if chess[ni][nj] != 2:  # 반대로 돌았는데 파란색이 아닌 경우
            infos[horse_no] = [ni, nj, d]  # 기존 말의 정보 수정; 좌표, 방향 수정
            horse_info[ni][nj] += now_horse  # 말 위에 얹기



def move_horses():
    for i in range(1, k+1):  # 1번부터 k까지 차례로 이동
        hi, hj, hd = infos[i]  # 현재 말의 좌표와 방향
        now_horse = horse_info[hi][hj]  # 현재 말 위에 얼마나 얹혀져 있는 지
        ni, nj = hi + delta[hd][0], hj + delta[hd][1]
        # 인덱스 밖 or 파란색인 경우
        if ni < 0 or ni >= n or nj < 0 or nj >= n or chess[ni][nj] == 2:
            # 옮길 말 찾기
            if len(now_horse) == 1:  # 현재 말이 이번 칸의 유일한 말
                horse_info[hi][hj] = [i]
            elif len(now_horse) > 1:
                for z in range(len(now_horse)):
                    if now_horse[z] == k:
                        horse_info[hi][hj] = now_horse[:z] + now_horse[z+1:]

            oppo_d = (5 - hd) % 4
            oppo_i, oppo_j = hi + delta[oppo_d][0], hj + delta[oppo_d][1]
            infos[i][2] = oppo_d  # 방향은 반대로
            if not (0 <= oppo_i < n and 0 <= oppo_j < n): continue
            if chess[oppo_i][oppo_j] != 2:
                infos[i] = [oppo_i, oppo_j, oppo_d]  # 기존 말의 정보 수정; 좌표, 방향 수정
                horse_info[ni][nj] += [i]  # 말 위에 얹기

            # move_color(ni, nj, oppo_d, i, 2, [i])
            continue

        if chess[ni][nj] == 0 or chess[ni][nj] == 1:
            nnext = [i]
            if len(now_horse) == 1:
                horse_info[hi][hj] = []
            elif len(now_horse) > 1:
                for z in range(len(now_horse)):
                    if now_horse[z] == i:
                        # print(z, now_horse[z], i)
                        horse_info[hi][hj] = now_horse[:z]
                        nnext = now_horse[z:]
                        break

            if chess[ni][nj] == 1: nnext = nnext[::-1]
            horse_info[ni][nj] += nnext  # 말 위에 얹기
            for ho in nnext:
                infos[ho][0], infos[ho][1] = ni, nj
            # move_color(ni, nj, hd, i, chess[ni][nj], nnext)  # 인덱스 안일 때 흰, 빨, 파를 만났을 때


# input
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오-왼-위-아래 순
# oppo = {0: 1, 1: 0}
n, k = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(n)]
horse_info = [[[] for _ in range(n)] for _ in range(n)]
infos = {}
for x in range(1, k+1):
    r, c, d = map(int, input().split())
    infos[x] = [r-1, c-1, d-1]
    horse_info[r-1][c-1] = [x]

# print(infos)  # {1: [1, 0, 0], 2: [2, 1, 2], 3: [1, 1, 0], 4: [3, 0, 1]}

turn = 0
while True:
    turn += 1
    move_horses()
    for elem in horse_info:
        print(elem)
    print(infos)
    print()
    if turn == 2:
        # for elem in horse_info:
        #     print(elem)
        print(infos)
        break
