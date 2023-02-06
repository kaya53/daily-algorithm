import sys

sys.stdin = open('input.txt')


def row_sum():
    max_sum = 0
    for i in range(100):
        sum_r = 0
        for j in range(100):
            sum_r += arr[i][j]
        if max_sum < sum_r:
            max_sum = sum_r
    return max_sum


def col_sum():
    max_sum = 0
    for i in range(100):
        sum_c = 0
        for j in range(100):
            sum_c += arr[j][i]
        if max_sum < sum_c:
            max_sum = sum_c
    return max_sum


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_row = row_sum()
    max_col = col_sum()
    ## 여기까지 row_sum, col_sum 중 최대는 나왔을 것

    max_left = max_right = 0
    for i in range(100):
        max_left += arr[i][i]
        max_right += arr[i][99-i]

    max_res = max_row
    for num in [max_col, max_left, max_right]:
        if max_res < num:
            max_res = num
    print(f'#{tc} {max_res}')