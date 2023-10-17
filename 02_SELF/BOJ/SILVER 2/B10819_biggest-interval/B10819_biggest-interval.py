# 소요시간 20분 python 152ms
# 조합 문제
import sys

sys.stdin = open('input.txt')


def comb(idx, n, nums, choice):
    global mmax

    if idx == n:
        tot = 0
        for i in range(n-1):
            tot += abs(nums[choice[i]] - nums[choice[i+1]])
        if mmax < tot:
            mmax = tot
        return

    for i in range(n):
        if i in choice: continue
        choice[idx] = i
        comb(idx+1, n, nums, choice)
        choice[idx] = -1


def solution(n, nums):
    comb(0, n, nums, [-1] * n)


mmax = 0
N = int(input())
ls = list(map(int, input().split()))
solution(N, ls)
print(mmax)