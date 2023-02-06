import sys

sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    mmax = max(arr)
    room = [[0] * mmax for _ in range(n)]
    
    # 상자가 쌓인 모양
    for idx, num in enumerate(arr):
        for i in range(num):
            room[idx][i] = 1

    # 각 행의 마지막 원소를 기준으로 열을 순회하면서 그 원소 아래로 0이 몇개 있는 지 세고 n에서 빼기
    res = 0
    max_res = 0

    for idx, num in enumerate(arr):
        last = arr[idx] - 1
        cnt = 0  # 자기 자신(현 위치) 빼주기
        for j in range(idx+1, n):  # 현 위치 아래에 있는 열 순회
            if room[j][last] == 0:
                cnt += 1
        if max_res < cnt:
            max_res = cnt

    print(f'#{tc} {max_res}')