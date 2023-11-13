# 소요시간 20분 pypy 120ms
# 피보나치와 비슷하게 생각하면 됨
# 점화식: 이전까지의 연산 결과(1,2,3 중 하나 더한 것)을 다음 연산에 사용한다
import sys

sys.stdin = open('input.txt')


def solution(num):
    global cnt

    if num == 0:
        cnt += 1
        return

    for k in [3,2,1]:
        if num - k < 0: continue
        solution(num-k)


T = int(input())
for _ in range(T):
    cnt = 0
    n = int(input())
    solution(n)
    print(cnt)
