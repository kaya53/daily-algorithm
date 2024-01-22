# 유의할 점
# left, right 조절 시 = 의 위치
# - 이 문제의 경우 인접 거리의 최댓값을 구하는 것이므로
# ⭐ "인접 거리를 늘릴 여지가 있을 때" 답을 갱신해 줘야 한다
import sys

sys.stdin = open('input.txt')


def solution(n, c, distance):
    distance.sort()

    l = 1
    r = distance[-1]-distance[0]
    answer = 0
    while l <= r:
        m = (l+r)//2
        now = distance[0]
        cnt = 1
        for i in range(1, n):
            if distance[i] - now >= m:
                now = distance[i]
                cnt += 1
        # 놓은 공유기 수가 c개이거나 더 많다 => 거리를 늘릴 수 있음
        # ; 이 문제는 인접 거리의 '최대값'을 구하는 것이므로
        # 거리를 늘릴 여지가 있는 곳에 =을 붙여야 한다
        if cnt >= c:
            l = m + 1
            answer = m
        else:
            r = m-1
    return answer



N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
k = solution(N, C, arr)
print(k)