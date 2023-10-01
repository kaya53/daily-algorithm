# 조합 코드 구현 pypy 1124ms
# 최대 21 C 10 => itertools가 좀 더 빠름
# 시간 초과가 안나려면
# 1. 처음에 antic는 무조건 선택하고 나머지 21개에 대해서만 조합을 돌려야 함
# 2. 그리고 k-5개만 뽑기


import sys

sys.stdin = open('input.txt')


def backtrack(depth, taught, k, words, ci, cand):
    global answer
    if depth == k-5:
        cnt = can_read(taught, words)
        if answer < cnt:
            answer = cnt
        return

    for i in range(ci, 21):
        ni = cand[i]
        taught[ni] = 1
        backtrack(depth+1, taught, k, words, i+1, cand)
        taught[ni] = 0


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

    for w in necessary: taught[w] = 1
    # print(words)
    cand = set([x for x in range(26)]) - necessary
    return backtrack(0, taught, k, words, 0, list(cand))


# for _ in range(3):
answer = 0
solution()
print(answer)