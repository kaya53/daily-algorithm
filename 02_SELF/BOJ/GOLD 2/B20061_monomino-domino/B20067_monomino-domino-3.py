import sys

sys.stdin = open('input.txt')


def put_block(b_type, ci, cj):
    pass


def get_score():
    cnt = 0
    return cnt


def remove_pastel():
    pass


N = int(input())
green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]

score = 0
for _ in range(N):
    block, si, sj = map(lambda x: int(x)-1, input().split())
    put_block(block, si, sj)
    score += get_score()
    remove_pastel()