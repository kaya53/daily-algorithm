import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def play_pinball(si, sj, sd):
    # 원래 방향대로 블럭을 만날 때까지 간다.
    # - 이동하다가 어느 시점이든 출발점을 만나면 끝남
    # 무언가를 만남
    # 1. 블럭을 만나면 그에 맞게 방향을 바꾼다.
    # 2. 웜홀을 만나면 대응되는 웜홀로 이동한다.
    # 3. 블랙홀을 만나면 끝난다.
    score = 0
    cd = sd
    ci, cj = si, sj
    while True:
        # 원래 방향대로 블럭 만날 때까지 이동
        ci, cj = ci + delta[cd][0], cj + delta[cd][1]
        if (ci, cj) == (si, sj): return score
        while not arr[ci][cj]:
            ci, cj = ci + delta[cd][0], cj + delta[cd][1]
            if (ci, cj) == (si, sj): return score # 시작점 만남

        # 블럭, 블랙홀, 웜홀 중 하나 만남
        now = arr[ci][cj]
        if now == -1: return score # 블랙홀
        elif 6 <= now <= 10:  # 웜홀
            for other in wormhole[now]:
                if (ci, cj) != other:
                    ci, cj = other
                    break
        elif 1 <= now <= 5:
            cd = block_dir[now][cd]
            score += 1


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
block_dir = {
    1: {1: 3, 0: 2, 2: 1, 3: 0},
    2: {0: 1, 1: 3, 2: 0, 3: 2},
    3: {0: 3, 1: 2, 2: 0, 3: 1},
    4: {0: 2, 1: 0, 2: 3, 3: 1},
    5: {0: 2, 1: 3, 2: 0, 3: 1}
}
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    fives = [5] * (N+2)
    arr = [fives] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [fives]

    # 웜홀 찾기
    wormhole = {}
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 6 <= arr[i][j] <= 10:
                if wormhole.get(arr[i][j], -1) == -1:
                    wormhole[arr[i][j]] = [(i, j)]
                else:
                    wormhole[arr[i][j]].append((i, j))
    # print(wormhole)
    mmax = 0
    # visited = set()
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j]: continue
            for d in range(4):
                res = play_pinball(i, j, d)
                # print(res, i, j, d)
                if mmax < res: mmax = res

    print(f'#{tc} {mmax}')
