import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

def solution(n, ls):
    tmp = []
    nge = [-1] * n
    for i in range(n):
        while tmp and ls[tmp[-1]] < ls[i]:
            nge[tmp.pop()] = ls[i]
        tmp.append(i)
        # print(i)
        # print(ls)
        # print(tmp)
        # print(nge)
    return nge


# for _ in range(3):
N = int(input().rstrip())
inp = list(map(int, input().rstrip().split()))
print(*solution(N, inp))