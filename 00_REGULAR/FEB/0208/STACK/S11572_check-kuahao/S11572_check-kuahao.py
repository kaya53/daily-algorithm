import sys

sys.stdin = open('input.txt')

from collections import deque


def kuahao(init):
    for elem in init:
        if elem in std:
            if elem == ')':
                if res and res[-1] == '(':
                    res.pop()
                else:
                    return 0
            elif elem == '}':
                if res and res[-1] == '{':
                    res.pop()
                else:
                    return 0
            else:
                res.append(elem)
    if not res:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    init = input()
    res = deque()
    std = ['(', ')', '{', '}']

    ans = kuahao(init)
    print(f'#{tc} {ans}')
