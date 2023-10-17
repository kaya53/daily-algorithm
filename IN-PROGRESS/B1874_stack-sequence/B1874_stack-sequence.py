# 소요시간 20분 python 176ms
# readline 쓰니까 시간이 1/20로 줄어듦
import sys
input = sys.stdin.readline


def solution(n, nums):
    stack = []
    res = []
    order = []
    idx = 0
    for num in nums:
        if idx < num:
            for i in range(idx+1, num+1):
                stack.append(i)
                order.append('+')
            idx = num
        if stack and stack[-1] == num:
            res.append(stack.pop())
            order.append('-')
    if res == nums:
        for o in order:
            print(o)
        return
    print('NO')


N = int(input())
ls = [int(input()) for _ in range(N)]
solution(N, ls)