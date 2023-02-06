import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 전체 배열, 파리채
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N-M+1):  # N=5, M=2 => 가로 줄: 0, 1, 2, 3
        for j in range(N-M+1):
            ssum = 0
            for k1 in range(M):
                for k2 in range(M):
                    ssum += arr[i+k1][j+k2]
            if max_sum < ssum:
                max_sum = ssum
    print(f'#{tc} {max_sum}')
    
    
    # 슬라이딩 윈도우
    # for i in range(N-M+1):  # N=5, M=2 => 가로 줄: 0, 1, 2, 3
    #     # ssum = arr[i][0] + arr[i][1] + arr[i+1][0] + arr[i+1][1]  # 문제 부분
    #
    #     for j in range(N-M):
    #         for k in range(M):
    #             ssum -= arr[i+k][j]
    #             ssum += arr[i+k][j+M]
    #             if max_sum < ssum:
    #                 max_sum = ssum
    