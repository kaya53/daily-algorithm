# python 256ms
# - 회의가 빨리 끝나는 순 > 빨리 시작하는 순으로 정렬해야 최적의 결과를 얻을 수 있음
# - 이렇게 정렬하고 나면 o(n)으로 해결할 수 있다
import sys
sys.stdin = open('input.txt')

def solution():
    n = int(input())
    times = [tuple(map(int, input().split())) for _ in range(n)]
    times.sort(key=lambda x: (x[1], x[0]))

    answer = 1
    std = times[0][1]
    for i in range(1, n):
        s, e = times[i]
        if s >= std:
            answer += 1
            std = times[i][1]
    return answer


print(solution())