import sys
#sys.stdin = open('03_11518_input.txt', 'r')

# 김성현 프로님
def code_01_before():
    T = int(input())
    for test_case in range(1, T+1):
        # 입력, 처리, 출력
        n, m = map(int, input().split())
        lst = list(map(int, input().split()))
        cnt = sum(lst[:m])
        mxnum = cnt
        minum = cnt
        for j in range(m, n):
            if cnt > mxnum:
                mxnum = cnt
            elif cnt < minum:
                minum = cnt
            cnt += lst[j] - lst[j - m]
        if cnt > mxnum:
            mxnum = cnt
        elif cnt < minum:
            minum = cnt
        print(f'#{test_case} {mxnum - minum}')


def code_02():
    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        aa = list(map(int, input().split()))
        a = sum(aa[:m])  # 맨 처음 m 개 데이터의 합 - 현 window 위치 [0 ~ m-1]
        maxx = a
        minn = a
        for i in range(n - m):
            a = a - aa[i] + aa[m + i]
            if a > maxx: maxx = a
            if a < minn: minn = a
        print(f'#{test_case} {maxx - minn}')

def code_02_after():
    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        aa = list(map(int, input().split()))
        a = sum(aa[:m])  # 맨 처음 m 개 데이터의 합 - 현 window 위치 [0 ~ m-1]
        maxx = a
        minn = a
        for i in range(n - m):
            a = a - aa[i] + aa[m + i]
            if a > maxx: maxx = a
            if a < minn: minn = a
        print(f'#{test_case} {maxx - minn}')


def solve_03_1(aa, n, m):
    a = sum(aa[:m])  # 맨 처음 m 개 데이터의 합 - 현 window 위치 [0 ~ m-1]
    maxx = a
    minn = a
    for i in range(n - m):
        a = a - aa[i] + aa[m + i]
        if a > maxx: maxx = a
        if a < minn: minn = a
    return maxx - minn

def solve_03_2(aa, n, m):
    a = sum(aa[:m])
    result = [0] * (n - m + 1)
    result[0] = a
    for j in range(n - m):
        a += (aa[j + m] - aa[j])
        result[j+1] = a
    result.sort()
    return result[-1] - result[0]


def code_03():
    T = int(input())
    for test_case in range(1, T + 1):
        n, m = map(int, input().split())
        aa = list(map(int, input().split()))
        sol = solve_03_2(aa, n, m)
        print(f'#{test_case} {sol}')


# 값의 목록이 있는 경우
def min_max_01(a):
    minV = maxV = a[0]   # 초기값을 목록의 첫 번째 값으로!
    for value in a[1:]:
        if value > maxV:
            maxV = value
        elif value < minV:
            minV = value
    return minV, maxV

# 값의 목록이 없는 경우 - 데이터가 중간에 발생하고, 몇 번 발생할지 모름
def min_max_02():
    # 초기값을 발생가능한 값의 범위를 고려하여 부여 (범위가 0 ~ 100 이라면 )
    minV = 101
    maxV = -1
    while True:
        value = int(input())
        if value == 10000: break
        # if ~ elif 구조를 사용하면 1개의 값만 있는 경우, 첫 값이 min인 경우 오류 발생
        # minV를 101 로 유지함
        # if ~  if ~  구조를 사용해야 함
        if value > maxV:
            maxV = value
        if value < minV:
            minV = value
    return minV, maxV

# 처음, 사이, 끝, 같은 값이 최댓값, 최솟값인 testcase를 만들어 test
# 데이터 개수 최소/최대 testcase 만들어 test  (import random 사용)
arr = [[3, 1, 2, 4, 7, 5, 6],
       [10, 1, 2, 4, 7, 5, 0],
       [0, 1, 2, 4, 7, 5, 10],
       [0, 0, 0],
       [6]]

minV, maxV = min_max_02()
print(minV, maxV)