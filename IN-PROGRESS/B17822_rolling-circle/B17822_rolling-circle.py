import sys

sys.stdin = open('input.txt')


def rotate(arr, x, direction, k):
    # 이 함수에서는 돌아간 원판 리턴하기
    idx = x
    while idx < x:
        if not direction:  # 시계
            pass
        else:  # 반시계
            pass
        idx += x


def calc(arr):
    # 모든 원판에 대해서 연산 수행
    pass


n, m, t = map(int, input().split())  # 격자 수, 원판 내 정수의 수, 총 회전 수
arr = [[0]] + [list(map(int, input().split())) for _ in range(n)]
infos = [list(map(int, input().split())) for _ in range(t)]

for info in infos:
    x, d, k = info  # x의 배수인 원판 돌리기, 돌릴 방향, 회전 수
    # 1. 원판을 돌린다.
    rotate(arr, x, d, k)
    # 2. 수를 지운다.
    calc(arr)