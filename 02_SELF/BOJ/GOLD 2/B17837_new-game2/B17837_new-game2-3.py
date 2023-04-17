import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def move_horse():
    for h in range(1, K+1):
        hi, hj, hd = horses[h]
        nhi, nhj = hi + delta[hd][0], hj + delta[hd][1]
        now = horses_dict[(hi, hj)]
        if len(now) >= 4: return False
        # print(now)
        idx = now.index(h)
        moved = now[idx:]  # 움직일 말들
        if moved == now:
            horses_dict.pop((hi, hj))
        else:
            horses_dict[(hi, hj)] = now[:idx]

        if arr[nhi][nhj] == 0:
            if white_and_red(moved, nhi, nhj) is False:
                return False
        elif arr[nhi][nhj] == 1:
            if white_and_red(moved[::-1], nhi, nhj) is False:
                return False
        elif arr[nhi][nhj] == 2:
            blue(moved, hi, hj, hd, h)


def white_and_red(moved, ni, nj):
    if horses_dict.get((ni, nj), -1) != -1:
        horses_dict[(ni, nj)] += moved
    else:
        horses_dict[(ni, nj)] = moved
    # 말 위치 정보 갱신
    for no in moved:
        horses[no][0], horses[no][1] = ni, nj
    # 4이상이면 리턴
    if len(horses_dict[(ni, nj)]) >= 4:
        return False


def blue(moved, ci, cj, d, no):
    d = oppo[d]
    ni, nj = ci + delta[d][0], cj + delta[d][1]
    # 방향 바꾸기
    horses[no][-1] = d
    if arr[ni][nj] == 0:
        white_and_red(moved, ni, nj)
    elif arr[ni][nj] == 1:
        white_and_red(moved[::-1], ni, nj)
    elif arr[ni][nj] == 2:
        # 다시 원래 대로 horses_dict 돌려 놓기
        if horses_dict.get((ci, cj), -1) != -1:
            horses_dict[(ci, cj)] += moved
        else:
            horses_dict[(ci, cj)] = moved


# input
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
oppo = [1, 0, 3, 2]
# for _ in range(5):
N, K = map(int, input().split())
blues = [[2] * (N+2)]
arr = blues + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + blues
horses = [0] * (K+1)
horses_dict = {}
for kk in range(1, K+1):
    r, c, dd = map(int, input().split())
    horses[kk] = [r, c, dd-1]
    horses_dict[(r, c)] = [kk]

# main
for turn in range(1, 1001):
    if move_horse() is False:
        print(turn)
        break
else:
    print(-1)