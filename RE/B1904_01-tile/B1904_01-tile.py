# 소요시간 의미없음 pypy 120ms
# 모듈러 연산의 특징
# ((a%n) + (b%n)) % n = (a+b)%n 이 성립한다
# 따라서 dp[i]를 계산할 때마다 모듈러 연산을 해줘도 답엔 이상이 없다
import sys

sys.stdin = open('input.txt')


def solution(n):
    ls = [0] * n
    ls[0] = 1
    if n > 1: ls[1] = 2
    for i in range(2, n):
        ls[i] = (ls[i-1]+ls[i-2])%15746
    return ls[n-1]


print(solution(int(input())))