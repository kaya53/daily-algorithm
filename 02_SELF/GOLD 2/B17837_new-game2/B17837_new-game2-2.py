import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def move_horse():
    for now in range(1, k+1):  # 1번 말부터 k번 말까지 이동
        hi, hj, hd = infos[now]

        # 이동할 말
        will_move = horse_arr[hi][hj]
        lenW = len(will_move)
        for z in range(lenW):
            if will_move[z] == now:
                horse_arr[hi][hj] = will_move[:z]
                will_move = will_move[z:]
                break

        # 이동하기
        ni, nj = hi + delta[hd][0], hj + delta[hd][1]
        # 인덱스 밖이거나 파란색이면
        if (ni < 0 or ni >= n or nj < 0 or nj >= n) or chess[ni][nj] == 2:
            opp_d = (5-hd) % 4
            nni, nnj = hi + delta[opp_d][0], hj + delta[opp_d][1]  # 반대 방향
            infos[now][2] = opp_d  # 일단 방향은 갱신
            # 바꾼 방향도 인덱스 밖이거나 파란칸이면
            if (nni < 0 or nni >= n or nnj < 0 or nnj >= n) or chess[nni][nnj] == 2:
                horse_arr[hi][hj] += will_move
                continue
            # 인덱스 밖이나 파란색이 아닌 경우 -> 좌표 갱신
            # 만약 가려는 칸이 빨강 칸이면 빨강칸 룰을 적용시켜야 함
            if chess[nni][nnj] == 1:
                will_move = will_move[::-1]
            horse_arr[nni][nnj] += will_move
            for m in will_move:
                infos[m][0], infos[m][1] = nni, nnj
            if len(horse_arr[nni][nnj]) >= 4: return False

        elif chess[ni][nj] == 0:
            horse_arr[ni][nj] += will_move
            for m in will_move:
                infos[m][0], infos[m][1] = ni, nj
            if len(horse_arr[ni][nj]) >= 4: return False

        elif chess[ni][nj] == 1:
            horse_arr[ni][nj] += will_move[::-1]
            for m in will_move:
                infos[m][0], infos[m][1] = ni, nj
            if len(horse_arr[ni][nj]) >= 4: return False
    return True


# input
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오-왼-위-아래 순; 0-1-2-3
# for _ in range(5):
n, k = map(int, input().split())
chess = [list(map(int, input().split())) for _ in range(n)]
infos = {}

horse_arr = [[[] for _ in range(n)] for _ in range(n)]  # 현재 말의 위치를 담고 있는 배열
for x in range(k):
    r, c, d = map(int, input().split())
    infos[x+1] = [r-1, c-1, d-1]
    horse_arr[r-1][c-1] = [x+1]

turn = 0
while True:
    turn += 1
    if turn > 1000:
        print(-1)
        break
    if not move_horse():
        print(turn)
        break

