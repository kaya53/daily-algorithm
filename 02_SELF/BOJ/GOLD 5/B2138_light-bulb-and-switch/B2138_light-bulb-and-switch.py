# 소요시간: 의미없음, python 120ms
# 새로운 아이디어를 배운 문제
# 그리디: 최적인 경우 하나로 경우의 수를 줄이는 것이 관건
# - 여기서는 스위치가 3개(양 끝은 2개)를 컨트롤하기 때문에 이 걸 하나로 줄여줘야 한다
# - 그러려면 두가지를 해야한다.
# 1. 첫 번째 스위치를 켤지 말지 결정
# - 이걸 안해주면 0번 전구가 영향 받는 스위치가 2개가 된다(1번 스위치, 2번 스위치)
# - 그렇기 때문에 이걸 처음에 결정해주지 않으면 한 스위치가 영향을 주는 전구를 하나로 줄일 수 없다
# - 켤 거면 켜고 나서 함수를 돌리고 아니면 그냥 돌려주면 된다
# - 그리고 그 두가지 경우 중 최소를 비교하면 된다
# 2. 현재 인덱스 직전 전구만 비교
# - 그래야 스위치 하나가 실질적으로 영향을 주는 전구가 하나가 된다

import sys

sys.stdin = open('input.txt')


def solution(now, target):
    now_copy = now[:]
    cnt = 0

    for i in range(1, N):
        if now_copy[i-1] == target[i-1]: continue
        cnt += 1
        for j in range(i-1, i+2):
            if j >= N: continue
            now_copy[j] ^= 1
        # print(now_copy)
    if now_copy == target: return cnt
    return 1000000


N = int(input())
bulbs = list(map(int, input()))
res = list(map(int, input()))
ans1 = solution(bulbs, res)

bulbs[0] ^= 1
bulbs[1] ^= 1

fin = min(solution(bulbs, res)+1, ans1)
if fin != 1000000: print(fin)
else: print(-1)

