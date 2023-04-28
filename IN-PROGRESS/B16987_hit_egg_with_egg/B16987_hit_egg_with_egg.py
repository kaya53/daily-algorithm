import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def hit_egg(idx, cnt):
    global mmax

    # cnt == N-1: 계란 하나 빼고 다 깨진 상황 => 어차피 또 못 깨므로 여기서 끝내도 됨
    if idx == N or cnt == N-1:
        mmax = max(mmax, cnt)
        return

    if s[idx] <= 0:  # 현재 계란이 이미 깨져있는 경우
        hit_egg(idx+1, cnt)

    else:
        for i in range(N):
            if idx == i or s[i] <= 0: continue
            s[idx] -= w[i]
            s[i] -= w[idx]
            n_cnt = cnt
            for k in [i, idx]:
                if s[k] <= 0: n_cnt += 1
            hit_egg(idx+1, n_cnt)
            s[idx] += w[i]
            s[i] += w[idx]

        # 온전한 계란이 없는 상황 => 모두 깨진 상황이니까 리턴하기
        # mmax = max(mmax, cnt)
        # return


# for _ in range(9):
N = int(input())
s = [0] * N
w = [0] * N
for nn in range(N):
    ss, ww = map(int, input().split())
    s[nn] = ss
    w[nn] = ww

mmax = 0
hit_egg(0, 0)
print(mmax)
