# 소요시간 20분 pypy 476ms
# 1. while left <= right에서 = 을 안붙이면 틀리고 붙이면 맞는다
# => 이 이유를 모르겠음
# 2. 잘리는 나무 연산을 줄일 수 있을 것 같은데 모르겠음
# => 속도 빠른 걸 보니까 Counter를 사용했음
# => Counter 쓰니까 python 420ms로 개선
import sys
from collections import Counter
# input = sys.stdin.readline

sys.stdin = open('input.txt')


def solution(n, m, trees):
    left = 0
    right = max(trees)
    # print(right)

    while left <= right:
        mid = (left + right) // 2
        tot = sum((h-mid)*i for h, i in trees.items() if h > mid)
        if tot > m:  # 같을 때는 여기서 같이 처리해줘도 됨 => 이유는 모르겠음
            left = mid + 1
        elif tot < m:
            right = mid - 1
        else:
            return mid
    return right


# for _ in range(2):
N, M = map(int, input().split())
A = Counter(map(int, input().split()))
r = solution(N, M, A)
print(r)