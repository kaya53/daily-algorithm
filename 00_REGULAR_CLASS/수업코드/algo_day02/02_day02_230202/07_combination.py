# 팩토리얼, 순열, 조합
# 순열(permutation) : 서로 다른 n개의 원소에서 r개를 중복없이 선택하는 것, 순서에 상관 있음
# 조합(combination) : 서로 다른 n개의 원소에서 r개를 중복없이 선택하는 것, 순서에 상관 없음
# A = {1, 2, 3, 4, 5}
# (1, 3, 5) (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1) : 6가지로 보는 것 - 순열
# (1, 3, 5) (1, 5, 3), (3, 1, 5), (3, 5, 1), (5, 1, 3), (5, 3, 1) : 1가지로 보는 것 - 조합


## 2개를 뽑는 조합 - index 사용
def combination_01():
    a = [1, 2, 3, 4]
    N = len(a)
    res = []
    # (1, 2), (1, 3), (1, 4)  # i=1, j=2, 3, 4
    # (2, 3), (2, 4)          # i=2, j=3, 4
    # (3, 4)                  # i=3, j=4
    #                         #
    for i in range(N-1):
        for j in range(i+1, N):
            res.append((a[i], a[j]))
    return res


## 3개를 뽑는 조합 - index 사용
def combination_01_B():
    a = [1, 2, 3, 4]
    N = len(a)
    res = []
    # (1, 2, 3), (1, 2, 4), (1, 3, 4)  # i=1, j=2, k=3, 4    i=1, j=3, k=4
    # (2, 3, 4)                        # i=2, j=3, k=4
    #                   # 없음
    #                   # 없음
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                res.append((a[i], a[j], a[k]))
    return res


# 2개를 뽑는 조합, 값을 사용함
def combination_02():
    a = [1, 2, 3, 4]
    r = 2
    c = []
    # (1, 2), (1, 3), (1, 4)  # i=1, j=2, 3, 4
    # (2, 3), (2, 4)          # i=2, j=3, 4
    # (3, 4)                  # i=3, j=4
    #                         #
    s = 0
    for i in a:
        s += 1
        for j in a[s:]:
            c.append([i, j])
    return c

#  이런 방식은 사용하지 않는 것이 좋음
def combination_03():
    a = [7, 8, 5, 2]
    r = 2
    c = []
    # (1, 2), (1, 3), (1, 4)  # i=1, j=2, 3, 4
    # (2, 1), (2, 3), (2, 4)          # i=2, j=3, 4
    # (3, 4)                  # i=3, j=4
    #                         #
    c = []
    for i in a:
        for j in a:
            if i >= j: continue
            #if i == j or [j, i] in c: continue
            c.append([i, j])
    return c


##  recursion (재귀 학습 후 살펴볼 것임)

def combination_03_recursion():
    b = []
    c = []

    def combination_03(level, llist, num):
        # llist는 원하는 배열, num은 원하는 쌍 수
        if level == 3:
            c.append(b)
            print(b)
            return
        for i in range(level, len(llist) - num + 1 + level):
            if b:
                if llist[i] == b[-1]:
                    continue
            b.append(llist[i])
            combination_03(level + 1, llist, num)
            b.pop()

    combination_03(0, [1, 2, 3, 4], 3)

def combination_04_recursion():
    # 재귀
    p = []
    arr = []

    def combination(n, m, start):
        if len(arr) == m:
            p.append(tuple(arr))
            return

        for i in range(start, n + 1):
            if i not in arr:
                arr.append(i)
                combination(n, m, i + 1)
                arr.pop()

    combination(4, 3, 1)
    print(p)
