# 소요시간 10분 python 40ms
# 1000개를 다 저장해 두지 말고 필요한 만큼만 저장해놓자
import sys

sys.stdin = open('input.txt')


def solution(start, end):
    idx = 0
    ls = [0] * (end-start+1)
    num = 1
    while True:
        for _ in range(num):
            if idx >= start-1:
                ls[idx-start+1] = num
            idx += 1
            if idx == end:
                return sum(ls)
        num += 1


s, e = map(int, input().split())
print(solution(s, e))