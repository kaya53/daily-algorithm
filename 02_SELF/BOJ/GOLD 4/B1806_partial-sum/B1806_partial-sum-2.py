# 소요시간: 의미 없음 pypy 140ms
# 투포인터 사용
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def func():
    start = end = 0
    res = 100000
    tot = nums[0]
    while start <= end < N:
        if tot >= S:
            if res > end-start+1:
                res = end-start+1
            # 부분 길이를 줄여본다
            tot -= nums[start]
            start += 1
        else:
            # 부분 길이를 늘려본다
            end += 1
            if end < N: tot += nums[end]
    return res


N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

ans = func()
print(ans if ans != 100000 else 0)
print(sum(nums))