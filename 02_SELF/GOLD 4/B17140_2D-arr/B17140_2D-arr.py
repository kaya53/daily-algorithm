import sys

sys.stdin = open('input.txt')

from collections import Counter

# r 연산
def calc_r(lenR, lenC, arr, flag):
    # 열도 100까지 자르기
    new_arr = [[] for _ in range(min(lenR, 100))]
    len_ls = []
    if lenR > 100: # 100개 자르기
        arr = [arr[i][:100] for i in range(min(lenR, 100))]
    max_len = lenC
    for r in range(lenR):
        now = arr[r]
        # cnt_ls = [0] * 101  # 0부터 100까지 세기
        # 각 행의 숫자 세기
        # print(tmp)  # Counter({1: 2, 2: 1})
        tmp = list(Counter(now).items())
        # print(lst)
        tmp.sort(key=lambda x: (x[1], x[0]))
        for el in tmp:
            if not el[0]: continue
            new_arr[r] += el
        # 행의 최대 길이
        len_ls.append(len(new_arr[r]))

    # 0 붙이기
    max_len = max(len_ls)
    for nr in range(len(len_ls)):
        new_arr[nr] += [0]*(max_len - len_ls[nr])

    if flag:
        return list(map(list, zip(*new_arr)))
    return new_arr


# for _ in range(7):
R, C, K = map(int, input().split())  # arr[r][c] == k(일때 까지 최소 시간
R -= 1
C -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
while True:
    try:  # r,c가 현재 배열 크기보다 큰 경우
        if arr[R][C] == K or time > 100: break
    except: pass
    time += 1
    # 1. r / c 연산에 중 어떤 것을 할 지 정한다.
    if len(arr) >= len(arr[0]):
        flag = False
    else:
        flag = True
        arr = list(map(list, zip(*arr)))
    arr = calc_r(len(arr), len(arr[0]), arr, flag)

if time > 100:
    print(-1)
else:
    print(time)