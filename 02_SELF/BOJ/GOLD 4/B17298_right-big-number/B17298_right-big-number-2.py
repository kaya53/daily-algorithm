import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(n, nums):
    answer = [-1] * n
    stack = []
    for i in range(n):
        curr = nums[i]
        while stack and nums[stack[-1]] < curr:
            answer[stack.pop()] = curr
        stack.append(i)
    return answer


print(*solution(int(input()), list(map(int, input().split()))))