import sys

sys.stdin = open('sample_input_bus.txt')


def charge_cnt(station):
    bus = cnt = 0
    while bus < N:
        for i in range(bus + K, bus, -1):
            if i in station:
                cnt += 1
                bus = i
                break
        else:
            return 0
        if bus + K >= N:
            return cnt
    # return cnt  # 여기는 불필요한 부분임


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    # print(K, N, M, station)
    res = charge_cnt(station)
    print(f'#{tc} {res}')
