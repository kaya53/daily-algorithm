# 소요시간 1시간: pypy 292ms
# 스택을 사용해야 하는 이유
# - 주어진 문자열의 길이가 최대 1,000,000임 => for문으로 보면 터진다
# - stack으로 보면 O(N)으로 끝낼 수 있다
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

std = list(input().rstrip())
bomb = list(input().rstrip())
next_stack = []
M = len(bomb)
while std:
    next_stack.append(std.pop())
    if next_stack[-1] == bomb[0]:
        if len(next_stack) < M or next_stack[-1:-1-M: -1] != bomb: continue
        for _ in range(M):
            next_stack.pop()
    # print(next_stack)

print(''.join(next_stack[::-1]) if next_stack else 'FRULA')





