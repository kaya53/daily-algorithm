# 소요시간 1시간 30분 : pypy 272ms, python 1532ms
# -get_cnt 함수 사용 => pypy 260ms
# 바뀐 결과가 조건에 맞는 지는 결과값을 컨트롤할 떄 확인해 준다!
# 그 전에 확인하면 오류가 발생할 수 있다
# => 일단 다 다음으로 넘기고(넘길 때 확인해야 하는 게 아니면) 종료 조건에서 최종적으로 검사한다
import sys

sys.stdin = open('input.txt')


def get_cnt():
    arr = [[0] * 10 for _ in range(10)]
    for me in range(10):
        me_bin = std[me]
        for you in range(10):
            if me == you: continue
            you_bin = std[you]
            cnt = 0
            for k in range(7):
                if me_bin[k] != you_bin[k]: cnt += 1
            arr[me][you] = cnt
    return arr


def dfs(cnt, idx, num):  # 남은 반전 횟수, 현재 숫자 idx, 경우의 수
    global res

    if idx >= len(num):
        # res를 올릴 때 반전된 숫자가 조건에 맞는 지 검사
        if int(num) != X and 1 <= int(num) <= N: res += 1
        return  # 모든 숫자를 다 봤으면 리턴

    me = int(num[idx])
    for you in range(10):
        if me == you: # 지금 단계에선 안바꾸고 다음 단계에서 바꿀 수도 있으니까
            dfs(cnt, idx+1, num)
        else:
            if board[me][you] <= cnt:  # cnt 이하의 횟수로 반전할 수 있으면
                new_num = num[:idx] + str(you) + num[idx+1:]
                # 여기서 다음 dfs를 넘길 때 new_num이 1 ~ N인지를 검사하면
                # 00인 경우에 넘어가지 않는다 => 마지막 최종에서 res를 늘려줄 때 검사하는 것이 맞음
                dfs(cnt - board[me][you], idx + 1, new_num)


# 전체 층수, 자리수, 바꿀 최대 led 수, 현재 층
# for _ in range(5):
N, K, P, X = map(int, input().split())
std = ['1110111', '0010010', '1011101', '1011011', '0111010',
       '1101011', '1101111', '1010010', '1111111', '1111011']

nx = str(X)
if len(str(X)) < K: nx = '0'*(K-len(nx)) + nx

# 한 수가 다른 한 수로 바꾸는 데 몇 번의 반전이 필요한 지 미리 구해놓는다
board = get_cnt()

res = 0
dfs(P, 0, nx)
print(res)
