# 소요시간 5분 python 44ms
# 유의할 점: 마지막 리턴할 때 string인 상태로 하면 01과 같이 될 수도 있으니
# int로 변환해서 리턴한다
import sys

sys.stdin = open('input.txt')


def solution(x, y):
    revX = x[::-1]
    revY = y[::-1]
    return int(str(int(revX)+int(revY))[::-1])


# for _ in range(5):
print(solution(*input().split()))
