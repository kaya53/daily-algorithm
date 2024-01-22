# 소요시간 30분 python 100ms
# 이분 탐색 시도하다가 투포인터로 푼 이유
# - 모든 용액을 탐색해야 하는데, 이분 탐색으로 하니까 모든 인덱스를 다 탐색할 수 없었음
import sys

sys.stdin = open('input.txt')


def solution(n, liquid):
    left = 0
    right = n-1

    r1, r2 = liquid[left], liquid[right]
    near = 2000000000
    # 같은 경우도 확인하면 left, right가 같은 경우도 체킹이 되는 데
    # 이건 문제 조건 상 말이 안되므로 = 을 뺀다
    while left < right:
        # mid = (left + right) // 2
        vl, vr = liquid[left], liquid[right]
        # print(vl, vr)
        tot = vl+vr
        if near > abs(tot):
            near = abs(tot)
            r1, r2 = vl, vr
            if tot == 0:
                return r1, r2

        if tot <= 0:
            left += 1
        else:
            right -= 1
    return r1, r2


# for _ in range(5):
k = solution(int(input()), list(map(int, input().split())))
print(*k)