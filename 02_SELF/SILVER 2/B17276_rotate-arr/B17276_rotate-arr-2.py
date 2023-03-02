import sys

sys.stdin = open('input.txt')

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for _ in range(abs(d) // 45):
        for i in range(n//2): # 0, 1, 2
            tmp1 = n // 2
            tmp2 = n - i - 1
            # 반시계
            if d < 0:
                arr[i][i], arr[i][n//2], arr[i][n-i-1], arr[n//2][n-i-1], arr[n-i-1][n-i-1], arr[n-i-1][n//2], arr[n-i-1][i], arr[n//2][i] \
                    = arr[i][n//2], arr[i][n-i-1],arr[n//2][n-i-1], arr[n-i-1][n-i-1], arr[n-i-1][n//2], arr[n-i-1][i], arr[n//2][i], arr[i][i]
            else:
                arr[i][i], arr[i][n//2], arr[i][n-i- 1], arr[n//2][n-i-1], arr[n-i-1][n-i-1], arr[n-i-1][n//2], arr[n-i-1][i], arr[n//2][i] \
                    = arr[n//2][i], arr[i][i], arr[i][n//2], arr[i][n-i-1], arr[n//2][n-i-1], arr[n-i-1][n-i-1], arr[n-i-1][n//2], arr[n-i-1][i]

    for elem in arr:
        print(' '.join(map(str, elem)))