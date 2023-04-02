import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def spring_summer():
    global tree_cnt

    dead_tree = []
    for i in range(N):
        for j in range(N):
            if not tree[i][j]: continue
            while tree[i][j]:
                for _ in range(len(tree[i][j])):
                    now_age = tree[i][j].pop()
                    if nutri[i][j] >= now_age:
                        nutri[i][j] -= now_age
                        tree[i][j].appendleft(now_age+1)
                    else:
                        dead_tree.append((i, j, now_age))
                break  # 한 번 돌고 끝내기

    if dead_tree: # 여름
        for dei, dej, d_age in dead_tree:
            nutri[dei][dej] += d_age // 2
            tree_cnt -= 1


def autumn_winter():
    global tree_cnt

    for i in range(N):
        for j in range(N):
            nutri[i][j] += winter_nutri[i][j]  # 겨울
            # 가을
            if not tree[i][j]: continue
            for t_age in tree[i][j]:
                if t_age % 5: continue
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                    tree_cnt += 1
                    tree[ni][nj].append(1)


delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
# for _ in range(8):
N, M, K = map(int, input().split())
winter_nutri = [list(map(int, input().split())) for _ in range(N)]
nutri = [[5] * N for _ in range(N)]  # 양분 격자; 초기값 5
# 처음에 deque * N 형태로 했었음
# 이렇게 하니까 모든 deque가 같은 메모리 주소를 가리켜서 동기화되어서 답이 안나왔음
tree = [[deque() for _ in range(N)] for _ in range(N)]
tree_cnt = 0
for _ in range(M):
    r, c, age = map(lambda x: int(x)-1, input().split())
    age += 1
    tree_cnt += 1
    tree[r][c].append(age)

for _ in range(K):
    spring_summer()
    autumn_winter()

print(tree_cnt)

# 딕셔너리로 하니까 불필요한 연산이 너무 많이 생김
# - 1. 딕셔너리를 순회할 때는 중간에 사이즈가 변하면 안되기 때문에
# - 더해주거나 빼주는 경우에 그 후보군을 따로 배열로 만들어놓고 딕셔너리 순회가 모두 끝나면 적용시켜야 함
# - 2. 해당 좌표가 딕셔너리의 키로 존재하는 경우, 안하는 경우로 나눠서 요소를 처리해야함
# => 이 문제의 경우 격자가 최대 10*10이기 때문에 격자를 여러 개 만들어 놓고 그 격자에 정보를 저장하는 게 낫다.
# 그리고 메모리 제한은 512로 평범한데 시간이 매우 짧으므로 사용하는 자료 구조를 줄이는 것보단
# 연산을 줄이는 게 여기선 맞는 방법이다.
