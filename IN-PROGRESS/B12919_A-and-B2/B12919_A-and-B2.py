import sys

sys.stdin = open('input.txt')


def recur(curr):
    global res
    if res: return
    # print(curr)
    if curr == S:
        res = 1
        return
    if len(curr) < len(S):return

    if curr[-1] == 'A':
        # print('A', curr)
        recur(curr[:-1])
    if curr[::-1][0] == 'B':
        # print('B', curr[::1][:-1])
        recur(curr[::-1][:-1])
    return False


for _ in range(3):
    S = list(input())
    T = list(input())
    lenT = len(T)
    res = 0
    recur(T)
    print(res)

