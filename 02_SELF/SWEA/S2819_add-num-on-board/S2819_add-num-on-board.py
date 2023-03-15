import sys

sys.stdin = open('sample_input.txt')


def comb(idx, ci, cj):
    global cnt
    if idx == 7:
        res.add(tuple(choice))
        return
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ci + di, cj + dj
        if ni < 0 or ni >= 4 or nj < 0 or nj >= 4: continue
        choice[idx] = arr[ni][nj]
        comb(idx + 1, ni, nj)
        # choice[idx] = 0  # 어차피 대체될 것이기 때문에 굳이 안넣어줘도 됨


t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    choice = [0] * 7
    cnt = 0
    res = set()
    for i in range(4):
        for j in range(4):
            comb(0, i, j)
    print(f'#{tc} {len(res)}')