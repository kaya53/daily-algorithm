# 소요시간 의미 없음 pypy 592ms
# stack 문제
import sys
sys.stdin = open('input.txt')


def solution(n, k, nums):
    nums = list(map(int, str(nums)))

    stack = []
    for num in nums:
        while stack and k and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if not k: return stack
    return stack[:-k]


# for _ in range(4):
N, K = map(int, input().split())
print(''.join(map(str, solution(N, K, int(input())))))