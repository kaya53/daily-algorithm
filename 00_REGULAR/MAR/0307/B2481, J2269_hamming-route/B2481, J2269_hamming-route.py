## bfs
# 인접, 최단 경로의 키워드로 알 수 있음
# 1. 시작점 1개
# 2. 끝점 1개 => 이런 것이 m번 반복
# 3. 인접; 해밍 거리가 1인 것
    # - 인접의 최대 수는 k개(코드의 자리수)만큼

## 해시 테이블; hash table -- 어떤 값에 o(1)로 접근 가능한 테이블
# - 어떤 값을 키(주소)로 활용하는 테이블
# - 딕셔너리 형태로 만들자
# - 코드끼리는 겹치지 않으니 이 코드를 키로 활용해보자
# h_table = { code : no }
# h_table.get(code, -1)

# 이 문제는 "시작점은 항상 1"이고 끝점이 다르니까
# bfs를 한 번만 해서 모든 점에 대해 해밍 경로를 알아낼 수 있다.
# visited = [0] * (n+1) ; 여기에 방문 표시 + 경로 표시


import sys

sys.stdin = open('input.txt')

a = 0b000
b = 0b100
# 해밍 거리가 1인 것만 찾기
tmp = a ^ b
# if not tmp & tmp-1: print(True)
# tmp & tmp-1 == 0이면 해밍 거리가 1

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[ht_table[start]] = -1
    while q:
        now = q.popleft()  # 현재 보고 있는 코드
        # 코드의 인접 보기
        # if ht_table.get('인접', -1) != -1이면 해당 부분에 있는 것
        # 있으면 q에 append하고 visited[다음 코드] = 현재 코드 번호
        for kk in range(k):
            adj = now ^ (1 << kk)  # 인접 코드
            # 여기서 불필요한 연산을 많이 해서 2348ms가 나왔는데 위의 코드로 고치니까 428ms 나옴
            # adj = int(bin(now ^ (1 << kk))[2:], 2)   
            if ht_table.get(adj, -1) != -1 and not visited[ht_table[adj]]:  # 테이블에 해당 인접이 존재
                q.append(adj)
                visited[ht_table[adj]] = ht_table[now]


# input
n, k = map(int, input().split())
ht_table = {}
start = 0
for x in range(1, n+1):
    inp = int(input(), 2)
    if x == 1: start = inp
    ht_table[inp] = x
m = int(input())  # 해밍 경로를 찾고자 하는 질의의 수
infos = [int(input()) for _ in range(m)]
# print(ht_table)  # {0: 1, 111: 2, 10: 3, 110: 4}
visited = [0] * (n+1)  # 방문 여부와, 지나온 경로를 표시할 배열

# 시작 코드 넣기
bfs(start)
# print(visited) # [0, -1, 4, 1, 3, 1]

for info in infos:
    res = []
    s = info
    # 여기서 경로가 없으면 -1을 출력하는 것도 구현해야 함
    cnt = 0
    while visited[s] != -1:
        if cnt > n:
            break
        cnt += 1
        res.append(s)
        s = visited[s]

    if len(res) > n:
        print(-1)
    else:
        print(1, *res[::-1])