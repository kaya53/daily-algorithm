import sys

sys.stdin = open('input.txt')


def check(idx):
    if idx == lenE:
        flag = True
        for d in range(1, 7):
            now = delta_count[d]
            if now.count(0) > 0:
                flag = False
        if flag:
            for dd in delta_count:
                print(dd)
            print()
        return

    for nnext in range(1, 7):
        now, cd = empty[idx]  # 현재 주사위 번호, 숫자가 없는 방향
        if not count[nnext] or not count[now]: continue
        if nnext in delta_count[now]: continue
        if delta_count[nnext][cd^1]: continue
        delta_count[now][cd] = nnext
        delta_count[nnext][cd^1] = now
        count[nnext] -= 1
        count[now] -= 1
        #other, od = found_other(now)
        #if (other, od) != (-1, -1):
            #delta_count[other][od] = now
            #delta_count[now][od^1] = other
        check(idx+1)
        delta_count[now][cd] = 0
        delta_count[nnext][cd^1] = 0
        count[nnext] += 1
        count[now] += 1


def found_other(now):
    for _ in range(count[now]):
        for z in range(1, 7):
            if z == now and now in delta_count[z]: continue
            for d in range(4):
                if not delta_count[z][d]:
                    other, od = z, d
                    return other, od
    return -1, -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
arr = []
for _ in range(3):
    board = []
    k = 1
    for n in range(6):
        inp = list(map(int, input().split()))
        for m in range(6):
            if inp[m] == 1:
                inp[m] = k
                k += 1
        board.append(inp)
    arr.append(board)

for board in arr:
    count = [0] + [4] * 6
    delta_count = [[0, 0, 0, 0] for _ in range(7)]
    for i in range(6):
        for j in range(6):
            if not board[i][j]: continue
            for k in range(4):
                ni, nj = i + delta[k][0], j + delta[k][1]
                if ni < 0 or ni >= 6 or nj < 0 or nj >= 6: continue
                if board[ni][nj]:
                    now = board[i][j]
                    other = board[ni][nj]
                    count[board[i][j]] -= 1
                    delta_count[now][k] = other
    # 빈 칸 찾기, (자기 번호, 방향)
    empty = []
    for r in range(1, 7):
        for c in range(4):
            if not delta_count[r][c]: empty.append((r, c))
    lenE = len(empty)
    for de in delta_count:
        print(de)
    print()
    # print(count)
    # check(0)