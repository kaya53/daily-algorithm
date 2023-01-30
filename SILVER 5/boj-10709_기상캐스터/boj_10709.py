import sys

sys.stdin = open('input.txt')

h, w = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(h)]

for i in range(h):
    res = -1
    c_flag = 0
    for j in range(w):
        if arr[i][j] == 'c':
            c_flag += 1
            res = 0
            print(res, end=' ')
        else:
            if c_flag == 0:
                print(-1, end=' ')
            elif c_flag > 0:
                res += 1
                print(res, end=' ')
    print()