import sys

sys.stdin = open('input.txt')

from collections import deque


# 1. 이동한다.
def moving(d,s):
    # visited = [[False] * N for _ in range(N)]
    len_c = len(cloud)
    cnt = 0
    while cnt < len_c:
        ci, cj = cloud.popleft()
        ni = ci + dir[d][0] * s
        nj = cj + dir[d][1] * s
        # 이렇게 하나 while을 쓰나 큰 차이가 없음
        if ni < 0 or ni >= N:
            ni %= N
        if nj < 0 or nj >= N:
            nj %= N
        cloud.append((ni, nj))
        cnt += 1  # 이동했으면 + 1
        # 2. 이동한 칸에 물 + 1 해준다
        raining(ni, nj)
    return

# 2. 물을 뿌린다.
def raining(ci, cj):
    area[ci][cj] += 1
    visited[ci][cj] = True
    return

# 3. 구름이 사라진다 - 나중에 필요할 때 하기
# 4. 물복사 버그 시전
def copy_water():
    while cloud:
        ci, cj = cloud.popleft()  # 여기서 pop하면서 구름이 사라짐
        for di, dj in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # 왼위 왼아래 오른위 오른아래
            ni = ci+di
            nj = cj+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if area[ni][nj]:
                area[ci][cj] += 1
    return

# 2. 새로운 구름 생성
def cloud_in():
    for i in range(N):
        for j in range(N):
            # cloud_x 배열을 활용하지 않으면 여기서 not in 연산자를 안써도 됨
            # O(N**2 * len(cloud))의 연산이 줄어듦
            # visited를 쓰면 그냥 다른 배열의 같은 인덱스니까 서로 비교만 하면 되는데
            # not in은 새로 순회를 해야 하니까 시간이 훨씬 많이 걸릴 것
            if not visited[i][j] and area[i][j] >= 2:
                area[i][j] -= 2
                cloud.append((i, j))  # 구름에 추가
    return


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]  # 비를 뿌릴 영역들
infos = [list(map(int, input().split())) for _ in range(M)] # (이동 방향, 이동할 칸 수)

cloud = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])  # 비바라기 시전 후 초기 구름 위치
# 이동 방향 : 왼 왼위 위 오른위 오른 오른아래 아래 왼아래(1~8)
dir = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# M번 이동 시작
for d, s in infos:
    # visited를 쓰니까 시간이 절반정도 줄어듦 - 왜? line 51-54에 적어놓음
    visited = [[False] * N for _ in range(N)]
    moving(d, s)
    copy_water()
    cloud_in()

res = 0
for i in range(N):
    ssum = 0
    for j in range(N):
        ssum += area[i][j]
    res += ssum
print(res)
# print(-1 % 5)



# 첫 제출 코드 - visited 안 쓴 코드
N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]  # 비를 뿌릴 영역들
infos = [list(map(int, input().split())) for _ in range(M)] # (이동 방향, 이동할 칸 수)

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
dir = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for d, s in infos:
    len_c = len(cloud)
    for i in range(len_c):
        ci, cj = cloud[i]
        ni = ci + dir[d][0]*s
        nj = cj + dir[d][1]*s
        while ni < 0: ni += N
        while ni >= N: ni -= N
        while nj < 0: nj += N
        while nj >= N: nj -= N
        cloud[i] = (ni, nj)
        area[ni][nj] += 1

    cloud_x = cloud
    for i in range(len_c):
        ci, cj = cloud[i]
        for di, dj in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:  # 왼위 왼아래 오른위 오른아래
            ni = ci+di
            nj = cj+dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
            if area[ni][nj]:
                area[ci][cj] += 1
    cloud = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in cloud_x and area[i][j] >= 2:
                area[i][j] -= 2
                cloud.append((i, j))

res = 0
for i in range(N):
    ssum = 0
    for j in range(N):
        ssum += area[i][j]
    res += ssum
print(res)