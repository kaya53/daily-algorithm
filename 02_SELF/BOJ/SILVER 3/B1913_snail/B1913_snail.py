import sys

input = sys.stdin.readline

def get_corners():
    std = 1
    si, sj = N//2, N//2
    d = 0
    corners = set()
    while (si, sj) != (0, 0):
        for _ in range(2):
            si, sj = max(0, si + delta[d][0]*std), max(0, sj + delta[d][1]*std)
            corners.add((si, sj))
            d = (d+1) % 4
            if (si, sj) == (0, 0): break
        std += 1
    return corners

def snail():
    si, sj = N//2, N//2
    # arr[si][sj] = 1
    d = 0
    num = 1
    res = (0, 0)
    while num <= N*N:
        # 현재 단계
        arr[si][sj] = num
        if num == target:
            res = (si+1, sj+1)

        # 다음 단계를 위한 갱신
        si, sj = si + delta[d][0], sj + delta[d][1]
        if (si, sj) in corners:
            d = (d+1) % 4
        num += 1
    return res


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(input())
target = int(input())
arr = [[0] * N for _ in range(N)]

corners = get_corners()
res = snail()
for a in arr:
    print(*a)
print(*res)
