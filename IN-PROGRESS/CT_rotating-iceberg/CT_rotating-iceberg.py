import sys

sys.stdin = open('input.txt')


def rotate(r):
    size = 2**(r-1)
    new = [[0] * L for _ in range(L)]
    for i in range(0, L, 2**r):
        for j in range(0, L, 2 ** r):
            delta = [(0, size), (size, 0), (-size, 0), (0, -size)]
            d = 0
            for ci in range(i, i+size+1):
                for cj in range(j, j+size+1):
                    new[ci+delta[d][0]][cj+delta[d][1]] = arr[ci][cj]
                    d += 1
    for ne in new:
        print(ne)
    return


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
rotation = list(map(int, input().split()))

L = 2**N
for r in rotation:
    for a in arr:
        print(a)
    print()
    rotate(r)

    break