import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline


def calc(ssum, now_cow):
    while ssum and now_cow:
        if ssum % 10 + now_cow % 10 >= 10:
            return False
        ssum //= 10
        now_cow //= 10
    return True


def comb(idx, weight_sum, cnt):
    global max_cnt
    # 가지치기
    # 보트에 탄 소 + 남은 소의 수(앞으로 태울 수 있는 소의 최대 수) < 현재 최대값이면 끝
    if cnt + n - idx <= max_cnt: return
    if idx >= n:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    if calc(weight_sum, weights[idx]):
        # if cnt + n - idx > max_cnt:  # 위의 가지치기를 아래에도 적용; 가능성이 있을 때만 태우러 보냄
        comb(idx+1, weight_sum + weights[idx], cnt + 1)
        comb(idx+1, weight_sum, cnt)
    else:
        comb(idx+1, weight_sum, cnt)


n = int(input())  # 소의 수
weights = [int(input()) for _ in range(n)]
max_cnt = 0
comb(0, 0, 0)

print(max_cnt)