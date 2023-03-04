import sys

sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row = [0]*n
    col = [0]*n
    
    # 초기 행과 열의 합 배열
    for r in range(n):
        for c in range(n):
            row[r] += arr[r][c]
            col[c] += arr[r][c]

    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for rr in range(r1-1, r2):
            row[rr] += (c2-c1+1)*v
        for cc in range(c1-1, c2):
            col[cc] += (r2-r1 + 1) * v

    print(*row)
    print(*col)