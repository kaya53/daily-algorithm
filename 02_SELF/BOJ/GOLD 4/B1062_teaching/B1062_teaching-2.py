# itertools 사용 pypy 836ms
# 최대 21 C 10
import sys

sys.stdin = open('input.txt')

from itertools import combinations

def can_read(taught, words):
    cnt = 0
    for word in words:
        for w in word:
            if not taught[w]: break
        else:
            cnt += 1
    return cnt


def solution():
    n, k = map(int, input().split())
    words = [list(map(lambda x:ord(x)-97, input())) for _ in range(n)]
    if k < 5: return 0  # 'anta, tica'도 읽을 수 없음

    taught = [0] * 26
    necessary = {0, 13, 19, 8, 2}

    for w in necessary:
        taught[w] = 1
    # print(words)
    cand = set([x for x in range(26)]) - necessary
    ls = combinations(cand, k-5)
    answer = 0

    for l in ls:
        print(l)
        for num in l:
            taught[num] = 1
        now = can_read(taught, words)
        if answer < now:
            answer = now

        for num in l:
            taught[num] = 0
    return answer


print(solution())
