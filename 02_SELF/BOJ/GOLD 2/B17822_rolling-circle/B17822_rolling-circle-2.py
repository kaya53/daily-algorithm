# 230522 python 172ms  - 1시간 가량 소요
# deque.rotate 다시 정리
# ZeroDivisionError!!!

import sys
from collections import deque

sys.stdin = open('input.txt')

def find():
    delete_set = set()
    whole = cnt = 0
    # 동시에 지워야 한다 => 지울 걸 지울 리스트에 놓기
    # 지울게 없으면 원판 전체의 수의 합의 평균 => delelte_ls가 비어있으면
    for i in range(1, N + 1):
        for j in range(M):
            if not circle[i][j]: continue
            whole += circle[i][j]
            cnt += 1

            # 인접 부분 수정
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                # j 부분 수정
                if ni < 1 or ni > N : continue
                # 어차피 nj가 인덱스 밖을 넘어가는 건 -1,0 밖에 없는 데 서로 연결되어 있으므로
                # 인덱스 에러를 방지하기 위해 이렇게 해준다.
                if nj == M: nj = 0
                # 여기 그냥 리스트에 append 해줘도 됨
                # 어차피 0으로 바꾸는 거니까 중복되어도 크게 상관 없음
                if circle[i][j] == circle[ni][nj]:
                    delete_set.add((i, j))
                    delete_set.add((ni, nj))
    if delete_set:
        for ri, rj in delete_set:
            circle[ri][rj] = 0
    else:
        if not cnt: return  # zero-division-error 해결
        mean = whole/cnt  # 그냥 float로; zero-division-error
        for ii in range(1, N+1):
            for jj in range(M):
                if not circle[ii][jj]: continue
                if circle[ii][jj] > mean: circle[ii][jj] -= 1
                elif circle[ii][jj] < mean: circle[ii][jj] += 1


# for _ in range(5):
N, M, T = map(int, input().split())
circle = [deque() for _ in range(N+1)]
for n in range(1, N+1):
    circle[n] = deque(list(map(int, input().split())))

# 돌리기 시작
for _ in range(T):
    x, d, k = map(int, input().split())
    # 1. x의 배수인 원판만 회전
    for cno in range(1, N+1):
        if cno % x: continue  # 배수가 아닌 원판
        if d == 0: circle[cno].rotate(k)
        elif d == 1: circle[cno].rotate(-k)

    # 2. 원판에 수가 남아 있으면 인접하면서 수가 같은 것을 찾는다.
    find()

res = 0
for c in circle:
    # print(c)
    res += sum(c)
print(res)