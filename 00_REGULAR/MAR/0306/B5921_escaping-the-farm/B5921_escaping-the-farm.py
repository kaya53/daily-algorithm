import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

def calc(arr):
    arr = list(map(list, map(str, arr)))

    minL = int(1e9)
    for elem in arr:
        if minL > len(elem):
            minL = len(elem)
    # print(len(arr), arr)  # 최소 자리수
    for i in range(minL, 0, -1):
        i *= -1
        digit_sum = 0
        for nums in arr:
            digit_sum += int(nums[i])
            if digit_sum >= 10:
                return False
    return True


def comb(idx, endnum, choice):
    global flag, res
    if idx == endnum:
        if calc(choice):
            flag = 1
            res = endnum
        return
    for c in range(idx, n):
        if not weights[c][1]:  # 아직 안올린 소
            weights[c][1] = 1
            choice[idx] = weights[c][0]
            comb(idx+1, endnum, choice)
            weights[c][1] = 0
            choice[idx] = 0


n = int(input())  # 소의 수
weights = [[int(input()), 0] for _ in range(n)]
flag = 0
res = 0
res_ls = []
for i in range(n, 0, -1):
    comb(0, i, [0] * i)
    if flag: break

print(res)
