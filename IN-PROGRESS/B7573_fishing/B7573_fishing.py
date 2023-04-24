import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def search(si, sj, width, height):
    global mmax
    now_cnt = 0
    # 여기를 for문을 2번써서 그물 내부를 모두 순회하니까 시간초과가 났음
    for fi, fj in fishes:
        if si <= fi <= si + width and sj <= fj <= sj+height: now_cnt += 1
    if mmax < now_cnt: mmax = now_cnt


def solve():
    global mmax
    for fi, fj in fishes:
        for w, h in net:  # 가능한 모든 그물 조합에 대해서
            for dj in [-1, 1]:
                tmpi = fi
                for kk in range(w + 1):  # 그물의 시작점을 왼쪽으로, 오른쪽으로 옮겨본다
                    if mmax == M: return  # 가지치기
                    if tmpi < 0 or tmpi >= N: break
                    search(tmpi, fj, w, h)
                    tmpi += dj
            for di in [-1, 1]:
                tmpj = fj
                for hh in range(h + 1):  # 그물의 시작점을 위쪽으로, 아래쪽으로 옮겨본다
                    if mmax == M: return  # 가지치기
                    if tmpj < 0 or tmpj >= N: break
                    search(fi, tmpj, w, h)
                    tmpj += di


N, I, M = map(int, input().split())
fishes = set()
for _ in range(M):
    fishes.add(tuple(map(lambda x: int(x)-1, input().split())))

# 가능한 그물 조합
net = [(k, (I//2)-k) for k in range(1, I//2)]

mmax = 0
solve()
print(mmax)
