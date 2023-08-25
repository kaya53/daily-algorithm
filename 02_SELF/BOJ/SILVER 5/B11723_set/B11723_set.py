# 소요 시간 40분: 시초/ 메초의 문제
# 시초/ 메초 대비에 쓴 방법
# 1. 주어지는 숫자가 1~ 20이므로 카운트 배열 사용
# 2. toggle에서는 ^ 연산자 사용
# 3. 함수로 따로 빼지 않음
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = [0] * 21

for _ in range(int(input())):
    inp = input().split()
    order = inp[0]
    if order == 'add':
        n = int(inp[1])
        if not S[n]: S[n] = 1
    elif order == 'remove':
        n = int(inp[1])
        if S[n]: S[n] = 0
    elif order == 'toggle':
        n = int(inp[1])
        S[n] ^= 1
    elif order == 'check':
        n = int(inp[1])
        if S[n]: print(1)
        else: print(0)
    elif order == 'all':
        for i in range(1, 21): S[i] = 1
    elif order == 'empty':
        for i in range(1, 21): S[i] = 0