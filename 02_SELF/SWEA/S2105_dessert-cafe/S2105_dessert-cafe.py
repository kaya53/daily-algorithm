import sys

sys.stdin = open('input.txt')


def go_cafe(choice, si, sj):
    cakes = set()  # 같은 숫자의 디저트 먹지 않게
    cakes_loc = set()  # 방문한 좌표 또 안가게
    tot_len = sum(choice)
    cnt = c = 0
    ci, cj = si, sj
    while cnt < tot_len:
        if choice[c] == 0: c += 1
        ci, cj = ci + delta[c][0], cj + delta[c][1]
        if ci < 0 or ci >= N or cj < 0 or cj >= N: return False # 격자 밖이면 다음 기준점을 보기
        # 갈 수 있는 상태
        if arr[ci][cj] not in cakes and (ci, cj) not in cakes_loc:
            cakes.add(arr[ci][cj])
            cakes_loc.add((ci, cj))
            choice[c] -= 1
            cnt += 1
        else: return False  # 이미 방문해서 갈 수 없는 상태
    return True


def solve():
    # 변의 길이 조합 구하기
    comb_ls = []
    for b1 in range(N - 2, 0, -1):
        if b1 == 1 or b1 == N - 2:
            choice = [b1, 1, b1, 1]
            comb_ls.append(choice)
            comb_ls.append(choice[::-1])
            continue
        for b2 in range(b1, 0, -1):
            choice = [b1, b2, b1, b2]
            comb_ls.append(choice)
            comb_ls.append(choice[::-1])

    comb_ls.sort(key=lambda x: -sum(x))
    # print(comb_ls)
    for ls in comb_ls:
        # if sum(ls) != 30: continue
        for i in range(N):
            for j in range(N):
                # print(sum(ls))
                if go_cafe(list(ls), i, j):
                    # print(ls)
                    return sum(ls)


delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
T = int(input())
for tc in range(1, T+1):
    # if tc > 1: break
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = solve()
    if res:
        print(f'#{tc} {res}')
    else:
        print(f'#{tc} -1')

