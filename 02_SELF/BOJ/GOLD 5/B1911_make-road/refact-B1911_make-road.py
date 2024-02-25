# 나머지를 사용하여 리팩토링 => python 통과 52ms
import sys

sys.stdin = open('input.txt')


def solution(n, l, pools):
    answer = 0

    pools.sort()
    last = 0  # 마지막 널빤지 위치
    for s, e in pools:
        if last > e: continue
        elif last < s:
            last = s
        dist = e - last
        r = 1 if dist % l else 0  #나누어 떨어지지 않으면 1개 더하기
        cnt = dist // l + r
        last += cnt*l  # 널판지 마지막으로 이동
        answer += cnt

    return answer


N, L = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, L, arr))