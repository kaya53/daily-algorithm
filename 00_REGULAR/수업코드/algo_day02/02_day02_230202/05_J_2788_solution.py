# 정올  (도약) - 2788
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2048

# 도약
def code_01():
    N = int(input())
    alist = [int(input())  for _ in range(N)]
    alist.sort()   # 오른쪽으로 이동  (숫자가 작은 것 --> 큰 것)

    cnt = 0
    for i in range(N-2):
        a1 = alist[i]
        for j in range(i+1, N-1):
            a2 = alist[j]
            for k in range(j+1, N):
                a3 = alist[k]
                step1, step2 = a2-a1, a3-a2
                if (a3-a2)>2*(a2-a1): continue
                if (a3-a2)<(a2-a1): continue
                #if (step2 > 2*step1) or (step2 < step1): continue
                cnt += 1
    print(cnt)

# 반복문 - 시간초과 - 원인이 있을까요?
def code_02():
    n = int(input())
    leaf = [int(input()) for _ in range(n)]
    leaf.sort()

    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                prev = leaf[j] - leaf[i]  # 위치를 고려해 보세요 (여기는 좋지 않음)
                next = leaf[k] - leaf[j]
                if prev * 2 >= next and prev <= next:
                    #print(leaf[i], leaf[j], leaf[k])
                    count += 1
    print(count)

##------------------------- 도약 반복 최적화 해보세요

# 결과 : 시간초과 발생
def code_03():
    # 입력값 받기
    n = int(input())
    leaf = []
    for _ in range(n):
        leaf.append(int(input()))
    leaf.sort()
    leaf_num = len(leaf)

    cnt = 0

    # 도약 횟수 세기
    for i in range(leaf_num - 2):
        for j in range(i + 1, leaf_num - 1):
            first = leaf[j] - leaf[i]
            for k in range(j + 1, leaf_num):
                second = leaf[k] - leaf[j]
                cond_1 = first <= second
                cond_2 = second <= first * 2
                if not (cond_1 and cond_2):
                    continue
                cnt += 1

    print(cnt)

def code_04():
    # 반복문 PyPy3으로 인터프리터 설정 시 시간 초과 안 함
    n = int(input())
    coor = []
    cnt = 0

    for i in range(n):
        coor.append(int(input()))

    coor.sort()

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                distance = coor[j] - coor[i]
                if distance <= coor[k] - coor[j] <= 2 * distance:
                    cnt += 1

    print(cnt)

def code_05():
    n = int(input())

    leaf = [0] * n
    for i in range(n):
        leaf[i] = int(input())
    leaf.sort()

    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            hop1 = leaf[j] - leaf[i]
            for k in range(j + 1, n):
                hop2 = leaf[k] - leaf[j]
                if hop1 * 2 < hop2:
                    break
                elif hop1 <= hop2:
                    cnt += 1
    print(cnt)



## ------  recursion & binary search

def code_02_DFS():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()

    answer = 0

    def DFS(x, dist, depth):
        global answer
        if depth == 2:
            answer += 1
            return
        for i in range(x + 1, N):
            tmp = arr[i] - arr[x]
            if dist <= tmp <= dist * 2 or dist == 0:
                DFS(i, tmp, depth + 1)

    for i in range(N - 2):
        DFS(i, 0, 0)
    print(answer)

def code_03_DFS():
    # 재귀
    n = int(input())
    leaf = []
    for _ in range(n):
        leaf.append(int(input()))

    leaf.sort()
    count = 0

    result = []

    def check(start):
        global count

        if len(result) == 3:
            prev = result[1] - result[0]
            next = result[2] - result[1]

            if prev <= next and prev * 2 >= next:
                count += 1
            return

        for i in range(start, n):
            result.append(leaf[i])
            check(i + 1)
            result.pop()

    check(0)

    print(count)

def code_04_BinarySearch():
    # 시간초과 해결
    N = int(input())
    leaps = [int(input()) for _ in range(N)]
    leaps.sort()

    def find_lower(s, e, d):
        ans = -1
        while s <= e:
            mid = (s + e) // 2

            if leaps[mid] >= d:
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans

    def find_upper(s, e, d):
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if leaps[mid] <= d:
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans

    n = len(leaps)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            d = leaps[j] - leaps[i]
            l = find_lower(0, n - 1, leaps[j] + d)
            if l < 0: break
            u = find_upper(0, n - 1, leaps[j] + d * 2)
            cnt += u - l + 1

    print(cnt)