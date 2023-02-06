import sys
input = sys.stdin.readline


def code_01():
    T = int(input())
    for test_case in range(1, T + 1):

        # 변수 입력받기
        n, d, k, c = [int(x) for x in input().split()]
        belt = []
        for _ in range(n):
            belt.append(int(input()))

        # Belt의 끝단에서 첫단으로 끊어지지 않고 넘어가도록 2배로 확장하기
        # k <= n 조건이 있으므로, 굳이 1번 이상 연결할 필요는 없음
        belt = belt * 2  ## belt * 2 개수가 적절한가?

        # 최초의 k개 초밥을 이용한 dictionary 생성하기
        first_sushi = belt[:k]
        sushi = {}
        for key in first_sushi:
            sushi.setdefault(key, 0)
            sushi[key] += 1

        # 무료쿠폰 초밥 1개를 먹은 개수에 추가하기
        sushi.setdefault(c, 0)  ##  무료쿠폰 초밥을 먼저 먹으면 좋지 않을까?
        sushi[c] += 1
        prev_cnt = len(sushi.keys())   ## len(sushi.keys()), len(sushi) 같음

        # sliding window로 belt를 탐색하기
        for i in range(k, len(belt) - k):
            sushi[belt[i - k]] -= 1
            if sushi[belt[i - k]] == 0:
                sushi.pop(belt[i - k])
            sushi.setdefault(belt[i], 0)
            sushi[belt[i]] += 1

            # 이전 값과 비교하여 더 큰 값을 출력하기
            curr_cnt = len(sushi.keys())
            if prev_cnt < curr_cnt: prev_cnt = curr_cnt

        print(prev_cnt)

def code_02():
    # 회전초밥
    n, d, k, c = map(int, input().split())

    # 초밥을 벨트에 올림
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    #  무료초밥
    hashTable = dict()
    hashTable[c] = 1

    # 최초의 k개 초밥을 이용한 dictionary 생성하기
    for i in range(k):
        if arr[i] not in hashTable:
            hashTable[arr[i]] = 0
        hashTable[arr[i]] += 1

    # 슬라이딩 윈도우 : 회전????  range(n)
    l, r = 0, k - 1
    result = -987654321
    for _ in range(n):
        hashKey = arr[l]
        result = max(len(hashTable), result)
        if hashKey not in hashTable: hashTable[hashKey] = 0
        hashTable[hashKey] -= 1
        if hashTable[hashKey] == 0: del hashTable[hashKey]
        l += 1
        r += 1
        if r >= n: r -= n
        if arr[r] not in hashTable: hashTable[arr[r]] = 0
        hashTable[arr[r]] += 1
    print(result)


def code_03():
    # 회전초밥
    from collections import deque

    # 입력 처리
    N, d, k, c = map(int, input().split())

    # 벨트 위 초밥 목록
    sushi = []
    for i in range(N):
        sushi.append(int(input()))

    lookup = [0] * (d + 1)
    cnt = 0
    max_cnt = 0

    # 쿠폰에 적힌 초밥을 룩업 테이블에 추가
    lookup[c] += 1
    cnt += 1
    max_cnt += 1

    # 슬라이딩 윈도우
    window = deque()

    # 처음 k개 초밥만큼 슬라이딩 윈도우에 넣기
    for i in range(k):
        window.append(sushi[i])
        if lookup[sushi[i]] == 0:
            cnt += 1
        lookup[sushi[i]] += 1

    if cnt > max_cnt:
        max_cnt = cnt

    # 슬라이딩 윈도우 움직이기
    for i in range(k, N + k):
        i %= N  # 모듈러 연산으로 원형 벨트 구현
        
        temp = window.popleft()
        if lookup[temp] == 1:
            cnt -= 1
        lookup[temp] -= 1
        
        window.append(sushi[i])
        if lookup[sushi[i]] == 0:
            cnt += 1
        lookup[sushi[i]] += 1
        
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


def code_04():
    
    # 회전 초밥
    def count_sushi(arr):
        cnt = len(set(arr))  ## set 연산에서 arr을 한번 순회
        if c not in arr: 
            cnt += 1  ## 여기서도 훑음
        return cnt

    ## 2531 회전 초밥은 통과하는데, 15961 회전 초밥은 시간 초과
    T = 4
    for _ in range(T):
        # 접시수, 초밥 가지수, 연속해서 먹는 초밥 수, 쿠폰 번호
        n, d, k, c = map(int, input().split())
        sushi = [int(input()) for _ in range(n)]

        # 초기 작업 - 쿠폰을 포함한 최초의 k개 초밥 먹고, 초밥 가짓수 반환
        sect = sushi[:k]
        cnt = count_sushi(sect)

        # 나올 수 있는 총 구간 n개의 크기를 갖는 배열을 만들고
        # 여기다가 각 구간이 가지는 가지수를 누적한다.
        cnt_ls = [cnt] + ([0] * (n - 1))

        # 0번 인덱스는 초기 작업에서 봤기 때문에 k번 인덱스부터 시작한다.
        # => 접시수와 구간의 수가 같을 때 1부터 시작하면 인덱스 에러가 남; 28번째 줄 n 자리에 8을 써서 그런 것이었음
        for i in range(k, n + k - 1):
            ri = i % n  # n이 얼마가 나오건 나머지 연산자 처리를 해줘서 한바퀴 돌 수 있게 해준다.
            sect.pop(0)  # 첫번째 원소를 빼고
            sect.append(sushi[ri])  # 그 다음 원소 집어넣기
            
            ## 여기서 바로 카운트를 해주면 시간이 줄 수 있다 ; max값 구할 때처럼 바로바로 갱신해 주면 된다
            cnt_ls[i - k + 1] = count_sushi(sect)  
        
        print(max(cnt_ls))


def code_05():
    # 회전 초밥(고)

    N, d, k, c = map(int, input().split())
    belt = [int(input()) - 1 for _ in range(N)]

    c -= 1
    cnt = 1
    sushi_dict = [0] * d
    # 쿠폰
    sushi_dict[c] = 1

    # 최초의 k개 초밥 종류 
    for i in range(k):
        cnt += not sushi_dict[belt[i]]   #  if sushi_dict[belt[i]] == 0: cnt += 1
        sushi_dict[belt[i]] += 1

    max_cnt = cnt
    i = 0
    while i <= N - 1:
        out = belt[i]
        in_ = belt[(i + k) % N]  # try except 로 바꿔도 된다
        if out != in_:
            sushi_dict[out] -= 1
            cnt -= not sushi_dict[out]
            cnt += not sushi_dict[in_]
            sushi_dict[in_] += 1
            if cnt > max_cnt:
                max_cnt = cnt
        # 가지치기
        if max_cnt == k + 1:
            break
        i += 1
    print(max_cnt)
