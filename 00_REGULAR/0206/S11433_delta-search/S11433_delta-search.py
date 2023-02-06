import sys

sys.stdin = open('ex01input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(5)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0
    for i in range(5):
        for j in range(5):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if (0 <= ni < 5) and (0 <= nj < 5):
                    cnt +=  abs(arr[ni][nj] - arr[i][j])
    print(f'#{tc} {cnt}')