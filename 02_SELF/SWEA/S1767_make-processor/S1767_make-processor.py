import sys

sys.stdin = open('sample_input.txt')


def find_processor(choice, arr, pcnt):
    global mmin

    for k in range(lenP):
        d = choice[k]
        si, sj = processor[k]
        while True:
            ni, nj = si + dir[d][0], sj + dir[d][1]
            if ni < 0 or ni >= n or nj < 0 or nj >= n: break  # 인덱스 밖으로 나갔다면 break
            if arr[ni][nj]:
                return 0
            arr[ni][nj] = 1
            pcnt += 1
            si, sj = ni, nj
    if pcnt and mmin > pcnt:
        mmin = pcnt
    return


def choose(idx):
    if idx == lenP:
        find_processor(choice, [i[:] for i in arr], 0)
        return

    for k in range(4):
        choice[idx] = k
        choose(idx + 1)
        choice[idx] = 0


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mmin = int(1e9)
    processor = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j]:
                processor.append((i, j))
    lenP = len(processor)
    choice = [0] * lenP
    choose(0)
    print(f'#{tc} {mmin}')