# 팩토리얼, 순열, 조합 - 순열
# 순열(permutation) : 서로 다른 n개의 원소에서 r개를 중복없이 선택하는 것, 순서에 상관 있음
# 조합(combination) : 서로 다른 n개의 원소에서 r개를 중복없이 선택하는 것, 순서에 상관 없음
# A = {1, 2, 3, 4, 5}
# (1, 3, 5) (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1) : 6가지로 보는 것 - 순열
# (1, 3, 5) (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1) : 1가지로 보는 것 - 조합

##  2개 뽑는 순열 - value 사용
def permutation_01_A():
    a = [1, 2, 3, 4]
    n = 2
    p = []
    # (1, 2), (1, 3), (1, 4)  # i=1, j=2, 3, 4
    # (2, 1), (2, 3), (2, 4)  # i=2, j=1, 3, 4
    # (3, 1), (3, 2), (3, 4)  # i=3, j=1, 2, 4
    # (4, 1), (4, 2), (4, 3)  # i=4, j=1, 2, 3
    for i in a:
        for j in a:
            if i == j: continue
            p.append([i, j])
    print(p)

##  2개 뽑는 순열 - index 사용
def permutation_01_B():
    a = [1, 2, 3, 4]
    N = len(a)
    p = []
    # (1, 2), (1, 3), (1, 4)  # i=1, j=2, 3, 4
    # (2, 1), (2, 3), (2, 4)  # i=2, j=1, 3, 4
    # (3, 1), (3, 2), (3, 4)  # i=3, j=1, 2, 4
    # (4, 1), (4, 2), (4, 3)  # i=4, j=1, 2, 3
    for i in range(N):
        for j in range(N):
            if i == j: continue
            p.append([a[i], a[j]])
    return p


## 3개 뽑는 순열
def permutation_02_A():
    a = [1, 2, 3, 4]
    n = 3
    p = []
    cnt = 0
    for i in a:
        for j in a:
            if i == j: continue
            for k in a:
                cnt += 1
                if j == k or i == k: continue
                p.append([i, j, k])
    print(cnt)
    return p


# [[1, 2, 3], [1, 2, 4], [1, 3, 2], [1, 3, 4], [1, 4, 2], [1, 4, 3],
# [2, 1, 3], [2, 1, 4], [2, 3, 1], [2, 3, 4], [2, 4, 1], [2, 4, 3],
# [3, 1, 2], [3, 1, 4], [3, 2, 1], [3, 2, 4], [3, 4, 1], [3, 4, 2],
# [4, 1, 2], [4, 1, 3], [4, 2, 1], [4, 2, 3], [4, 3, 1], [4, 3, 2]]

##  3개 뽑는 순열, 불필요한 반복을 포함하고, 불필요한 조건도 포함하고 있음
def permutation_02_B():
    a = [1, 2, 3, 4]
    n = 3
    p = []
    cnt = 0
    for i in a:
        for j in a:
            for k in a:
                cnt += 1
                if i == j or j == k or i == k or (i == j and j == k): continue
                p.append([i, j, k])
    print(cnt)
    return p



##  recursion (재귀 학습 후 살펴볼 것임)

def permutation_03_recursion():
    p = []
    arr = []
    # n개 데이터에서 m개 뽑기
    def permutation(n, m):
        global p, arr
        if len(arr) == m:
            p.append(tuple(arr))
            return

        for i in range(1, n + 1):
            if i not in arr:
                arr.append(i)
                permutation(n, m)
                arr.pop()

    permutation(4, 2)
    print(p)

def permutation_04_recursion():
    # N에 4, M에 3 넣으면 동일한 결과가 나옴
    N, M = map(int, input().split())  # N은 숫자의 총 개수들  M은 그 중 몇 개를 뽑을 것인지?
    check = []
    visited = [False] * (N + 1)  # True/False를 통해 append할 것인지 말 것인지

    def permutation_02(num):
        if num == M:  # M과 마주하면
            print(' '.join(map(str, check)))  # 결과 출력해내고
            return
        for i in range(1, N + 1):  # 1부터 N까지 visited에다 인덱스접근해서
            if visited[i] == False:  # False면
                visited[i] = True  # 방문처리해주고
                check.append(i)  # check에다 숫자 넣어주고
                permutation_02(num + 1)  # 재귀호출
                visited[i] = False  # 재귀호출 돌리다가 위에서 결과 출력되고 return되면 여기로 와짐
                check.pop()  # 위에서 False처리된거 pop시키고  다시 for문 루핑 시작

    permutation_02(0)