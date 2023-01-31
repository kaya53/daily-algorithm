# arr = [[i for i in range(5)] for _ in range(5)]
# print(arr)
# fliped_arr = list(map(list, zip(*arr)))
# print(fliped_arr)
import sys

sys.stdin = open('input.txt')

for _ in range(3):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    flipped_arr = [[0]*n or _ in range(n)]

    for i in range(n):
        for j in range(n):
            flipped_arr[j][i] = arr[i][j]
    # flipped_arr = list(map(list, zip(*arr)))  # 얘가 오히려 메모리와 시간이 조금 더 걸렸음
    # print(flipped_arr)
    tmp = [[], []]
    for i in range(n):
        if sum(arr[i]) % 2:
            tmp[0].append(i)
        if sum(flipped_arr[i]) % 2:
            tmp[1].append(i)
    # print(tmp)

    if not tmp[0] and not tmp[1]:
        print('OK')
    elif len(tmp[0]) == 1 and len(tmp[1]) == 1:
        print(f'Change bit ({tmp[0][0]+1},{tmp[1][0]+1})')
    else:
        print('Corrupt')
