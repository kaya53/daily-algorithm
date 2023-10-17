# 소요시간 10분 python 48ms pypy 152ms
# 시키는 대로 하면 됨
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(n, orders):
    stack = []
    length = 0
    for order in orders:
        if order == 'pop':
            if stack:
                print(stack.pop())
                length -= 1
            else: print(-1)
        elif order == 'size':
            print(length)
        elif order == 'empty':
            if length: print(0)
            else: print(1)
        elif order == 'top':
            if stack: print(stack[-1])
            else: print(-1)
        else:
            k, v = order.split()
            stack.append(int(v))
            length += 1


N = int(input().rstrip())
ls = [input().rstrip() for _ in range(N)]
solution(N, ls)