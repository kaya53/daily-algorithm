import sys

sys.stdin = open('input.txt')


# 1. 범위가 정해져있음; 1000 ~ 9999
# 2. 소수라는 것은 "변하지 않는" 사실임
# => 이럴 때는 룩업 테이블을 쓰면 좋다; 사방 탐색할 때 만들어 놓는 dir 배열 같은 거

# 따라서 이 문제에서도 소수 판별할 때 룩업 테이블을 써보자
# 9000개 수에 대해서 판별해야 하기 때문에 효율적 방법이 필요함 -> 에라토스테네스의 체

# 로직
# 반복 횟수가 1개 버스에서 40번, 그리고 최소 몇번을 가야할 지 가늠이 힘들다
# 많은 수의 반복을 가정한다면 bfs를 사용하는 것이 안전
# bfs: 최단 경로
    # queue, 탑승했던 버스 다시 탑승 안하기(visited)

# 방문 표시 : 버스 번호를 index로 하는 배열 준비
# visited: 1차원 10000개 짜리 (해당 버스를 탔는 지, 안 탔는 지)
# 버스 환승 횟수(이동 횟수): visited 배열에 써도 되고, q에 달고 다녀도 됨
# 반환: 최소 환승 횟수
from collections import deque

t = int(input())
for _ in range(t):
    start, end = map(int, input().split())

    # 소수 판별하기
    sieve = [True] * 10000
    m = 5000 # 9000의 절반
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, 10000, i):
                sieve[j] = False

    prime_ls = [i for i in range(1000, 10000) if sieve[i]]
    # print(prime_ls)

    visited = [False] * 10000
    q = deque()
    q.append((start, 0))
    visited[start] = True
    mmin = int(1e9)
    while q:
        now, cnt = q.popleft()
        if now == end:
            if mmin > cnt:
                mmin = cnt
            break
        # 인접한 방향
        for i in range(4):
            start_ls = list(str(now))
            target = start_ls[i]  # 바꿀 자리
            for j in range(10):
                if not i and not j: continue
                if target == str(j): continue
                start_ls[i] = str(j)
                nextbus = int(''.join(start_ls))
                if nextbus in prime_ls and not visited[nextbus]:
                    visited[nextbus] = True
                    q.append((nextbus, cnt + 1))
    if mmin == int(1e9):
        print('Impossible')
    else:
        print(mmin)

# 인접한 노선
# for i in range(4):
#     std = 10**i
#     visited_adj = [0] * 10
#     for j in range(10):
#         nextbus = start + std
#         if not visited_adj[nextbus]:  # 아직 안갔으면
#             visited_adj[nextbus] = 1
#             q.append(nextbus)


