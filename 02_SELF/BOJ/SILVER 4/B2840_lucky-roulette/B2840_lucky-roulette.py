# 소요시간 20분 => python 64ms
# 유의할 점
# 룰렛 안에 알파벳이 여러 번 등장하지 않는 점도 고려해야 함
import sys

sys.stdin = open('input.txt')

from collections import deque


def solution():
    n, k = map(int, input().split())
    wheel = deque(['?'] * n)
    paper = [input().split() for _ in range(k)]

    check = [0] * 26
    for no, char in paper:
        no = int(no)
        wheel.rotate(no)
        # 이미 채워진 칸인데 다른 알파벳이 들어옴
        if wheel[0] != '?' and wheel[0] != char: return '!'
        # 이미 채워져있는 알파벳인데 또 들어옴
        if wheel[0] != char and check[ord(char)-65]: return '!'
        wheel[0] = char
        check[ord(char) - 65] = 1
    return ''.join(wheel)


# for _ in range(4):
print(solution())
