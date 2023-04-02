import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

def comb(idx, choice):
    if idx == K:
        # print(choice)
        rotate(choice, [x[:] for x in arr])
    for ni in range(K):
        if ni in choice: continue
        comb(idx+1, choice+[ni])


def rotate(choice, c_arr):
    global res

    for ch in choice:  # 회전 시작
        rr, cc, ss = infos[ch]
        size = 2*ss + 1
        tmp = [[0] * size for _ in range(size)]
        for idx in range(ss):
            si, sj = rr-ss+idx, cc-ss+idx
            ci, cj, cd = si, sj, 0
            while (ci, cj) != (si+1, sj):
                ni, nj = ci + delta[cd][0], cj + delta[cd][1]
                if ni < rr-ss+idx or ni > rr+ss-idx or nj < cc-ss+idx or nj > cc+ss-idx:
                    cd = (cd+1) % 4
                    ni, nj = ci + delta[cd][0], cj + delta[cd][1]
                tmp[ni-(rr-ss)][nj-(cc-ss)] = c_arr[ci][cj]
                ci, cj = ni, nj
            # 여기 아래 c_arr 부분에 처음에 arr이라고 잘못 써서 틀렸었음
            tmp[idx][idx] = c_arr[ci][cj]
        tmp[size//2][size//2] = c_arr[rr][cc]

        # tmp를 원래 배열에 붙이기
        for ti in range(size):
            for tj in range(size):
                c_arr[ti+rr-ss][tj+cc-ss] = tmp[ti][tj]

    min_sum = int(1e9)
    for cr in c_arr:
        ns = sum(cr)
        if min_sum > ns:
            min_sum = ns
    if res > min_sum:
        res = min_sum


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
infos = [0] * K
for kk in range(K):
    r, c, s = map(lambda x: int(x)-1, input().split())
    infos[kk] = (r, c, s+1)

res = int(1e9)
comb(0, [])
print(res)