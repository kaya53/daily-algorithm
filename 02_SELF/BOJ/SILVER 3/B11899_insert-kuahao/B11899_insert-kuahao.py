import sys

sys.stdin = open('input.txt')

from collections import deque

init = input().rstrip()
stack = deque()

cnt = 0
for elem in init:
    if not stack:
        stack.append(elem)

    else:
        if stack[-1] == '(':
            if elem == ')':
                stack.pop()
                continue
        stack.append(elem)
print(len(stack))