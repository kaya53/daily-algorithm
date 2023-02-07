import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())  # 연산자와 피연산자(+-/*)의합
    initial = input().split()
    nums = deque()
    operator = deque()

    for elem in initial:
        try:  # 숫자일 때 - if elem.isdecimal()도 사용가능
            nums.append(int(elem))
        except: # 연산자일 때
            num1 = nums.pop()  # 뒷수 - 먼저 나왔으니까
            num2 = nums.pop()  # 앞수 - 나중에 나왔으니까

            if elem == '+': res = num2 + num1
            elif elem == '-': res = num2 - num1
            elif elem == '*': res = num2 * num1
            else: res = num2 // num1
            nums.append(res)
    print(nums[0])