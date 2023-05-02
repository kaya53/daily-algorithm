# 재귀에서 생각해야 하는 것 => flat하게 봐야 함
# (cf) 반복
# - "단위 반복"이 무엇인가를 생각하는 것이 중요함
# - 2, 3개 정도 정해진 횟수만큼 반복되는 경우


# 함수 반복 수행; 함수가 한 번 동작할 때 어떤 일을 해야 하는 지 생각해야 함
# 나와 같은 형태의 함수가 반복되는 데 그 범위가 점점 작아지는 형태
# 반복이 몇 번이나 이루어질 지 모르는 경우에 사용; 경우에 따라 반복되는 횟수가 달라지는 경우


# 1. 함수의 정의/역할을 명확히 하기(유도 조건 부분)
    # what this function do => how는 생각할 필요 없음
# 2. 기저 조건(base case) 확인해야 함 => 끝을 낼 수 없으면 재귀를 짤 수 없음
# 3. 함수의 매개 변수(결정 요인)를 어떻게 설정할 것인가
    # 함수마다 변하는 부분이 생기기 때문에 이걸 다음 재귀에 전달해줘야 하므로

# 시간 복잡도; worst일 때
# 달걀 최대 7개씩(자기 자신 제외) => 각 단계마다 8개 다 봄 ; 7**8(약 570만)
# 시간 상 가능함

import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def hit_egg(idx, cnt):
    global mmax

    # cnt == N-1: 계란 하나 빼고 다 깨진 상황 => 어차피 또 못 깨므로 여기서 끝내도 됨
    # cnt == N: 가능한 모든 계란이 깨진 상황이니까 나머지 케이스를 볼 필요 없음
    if idx == N or cnt >= N-1:
        mmax = max(mmax, cnt)
        return

    if s[idx] <= 0:  # 현재 계란이 이미 깨져있는 경우
        hit_egg(idx+1, cnt)

    else:
        for i in range(N):
            if idx == i or s[i] <= 0: continue
            s[idx] -= w[i]
            s[i] -= w[idx]
            n_cnt = cnt
            for k in [i, idx]:
                if s[k] <= 0: n_cnt += 1
            hit_egg(idx+1, n_cnt)
            s[idx] += w[i]
            s[i] += w[idx]

        # 온전한 계란이 없는 상황 => 모두 깨진 상황이니까 리턴하기
        # mmax = max(mmax, cnt)
        # return

# for _ in range(9):
N = int(input())
s = [0] * N
w = [0] * N
for nn in range(N):
    ss, ww = map(int, input().split())
    s[nn] = ss
    w[nn] = ww

mmax = 0
hit_egg(0, 0)
print(mmax)