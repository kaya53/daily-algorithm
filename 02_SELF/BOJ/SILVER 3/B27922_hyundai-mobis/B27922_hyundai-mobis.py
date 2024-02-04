# 소요시간 20분 python 340ms, pypy 416ms
import sys

sys.stdin = open('input.txt')


def solution(n, k, scores):
    sa = sorted(scores, key=lambda x: (x[0]+x[1])*(-1))
    sb = sorted(scores, key=lambda x: (x[1]+x[2])*(-1))
    sc = sorted(scores, key=lambda x: (x[0]+x[2])*(-1))

    answer = 0
    for a, b, score in [(0, 1, sa), (1, 2, sb), (0, 2, sc)]:
        tot = 0
        for i in range(k):
            now = score[i]
            tot += now[a] + now[b]
        if answer < tot:
            answer = tot
    return answer


N, K= map(int, input().split())
S = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, K, S))