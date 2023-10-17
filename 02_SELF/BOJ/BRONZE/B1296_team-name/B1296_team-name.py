# 소요시간 20분 python 48ms
import sys

sys.stdin = open('input.txt')


def solution(y, n, ls):
    std = [0] * 4
    for c in y:
        if c == 'L': std[0] += 1
        elif c == 'O': std[1] += 1
        elif c == 'V': std[2] += 1
        elif c == 'E': std[3] += 1

    mmax = 0  # 나머지값으로 가능한 값 중 가장 작은 건 0
    res = ls[0]
    for strs in ls:
        cnt = std[:]
        for ch in strs:
            if ch == 'L': cnt[0] += 1
            elif ch == 'O': cnt[1] += 1
            elif ch == 'V': cnt[2] += 1
            elif ch == 'E': cnt[3] += 1
        val = 1
        for i in range(4):
            for j in range(i+1, 4):
                val *= (cnt[i] + cnt[j])
        val %= 100
        if mmax < val:
            mmax = val
            res = strs
    return res


# for _ in range(6):
Y = (input())
N = int(input())
inp = [input() for _ in range(N)]
inp.sort()  # 사전 순 출력
print(solution(Y, N, inp))