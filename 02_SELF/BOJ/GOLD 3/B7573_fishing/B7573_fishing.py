# 그리디 알고리즘 => 최적해를 구할 때 사용됨
# - 모든 경우를 다 따지지 않기 때문에 시간 상 유리함
# - 최대, 최소 등
# - 전체 중 가장 최선을 선택 => 해가 최선임을 잘 검증할 수 있어야함
# - 더이상 남은 부분 문제가 없을 때까지 계속 한다

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


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
            # for dj in [-1, 1]:
            tmpi = fi
            for _ in range(w + 1):  # 그물의 시작점을 왼쪽으로, 오른쪽으로 옮겨본다
                if mmax == M: return  # 가지치기
                if tmpi < 0 or tmpi >= N: break
                search(tmpi, fj, w, h)
                tmpi -= 1
            # for di in [-1, 1]: # 그물의 시작점을 위쪽으로, 아래쪽으로 옮겨본다 => 이건 위부터 쓸어내려오기 때문에 고려해줄 필요가 없다
            # tmpj = fj
            # for _ in range(h + 1):
            #     if mmax == M: return  # 가지치기
            #     if tmpj < 0 or tmpj >= N: break
            #     search(fi, tmpj, w, h)
            #     tmpj -= 1


N, I, M = map(int, input().split())
fishes = set()
for _ in range(M):
    fishes.add(tuple(map(lambda x: int(x)-1, input().split())))

# 가능한 그물 조합 ==> 해당 그물 길이에서 가능한 직사각형의 높이와 길이
net = [(k, (I//2)-k) for k in range(1, I//2)]

mmax = 0
solve()
print(mmax)
