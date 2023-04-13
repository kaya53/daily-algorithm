import sys

sys.stdin = open('input.txt')


def move():
    moved = {}
    for k, v in micros.items():
        ci, cj = k
        now_num, d = v

        # 이동
        ni, nj = ci + delta[d][0], cj + delta[d][1]
        if not ni or ni == N-1 or not nj or nj == N-1:
            now_num = int(now_num / 2)
            d = change[d]

        if moved.get((ni, nj), -1) == -1:
            moved[(ni, nj)] = [1, [(now_num, d)]]
        else:
            # 군집이 최대 1000개이기 때문에 매번 len()을 쓰면 시간이 걸릴 것이기 때문에
            # 군집이 추가될 때마다 개수를 갱신해주는 방식으로 함 => after_move 함수에서 사용
            moved[(ni, nj)][0] += 1  
            moved[(ni, nj)][1].append((now_num, d))

    return after_move(moved)


def after_move(moved):
    after = {}
    for k, v in moved.items():
        # ci, cj = k
        if v[0] == 1:  # 군집 하나
            after[k] = [*v[1][0]]
        else:  # 군집 여러개
            ssum = 0
            this_max = 0
            this_d = -1
            for num, d in v[1]:
                ssum += num
                if this_max < num:
                    this_max = num
                    this_d = d
            after[k] = [ssum, this_d]

    return after


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
change = [1, 0, 3, 2]
T = int(input())
for tc in range(1, T+1):
    # input
    N, M, K = map(int, input().split())
    micros = {}
    for _ in range(K):
        i, j, nn, dd = map(int, input().split())
        micros[(i, j)] = [nn, dd-1]

    # main
    for _ in range(M):
        micros = move()

    # output
    res = 0
    for val in micros.values():
        res += val[0]
    print(f'#{tc} {res}')