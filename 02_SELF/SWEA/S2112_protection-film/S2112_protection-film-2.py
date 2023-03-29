import sys

sys.stdin = open('input.txt')


def test(mtx):
    for j in range(W):
        i = 0
        while i <= D-K:
            ssum = 0
            for ni in range(i, i+K):
                ssum += mtx[ni][j]
            if ssum == 0 or ssum == K: break  # 통과됨
            i += 1
        else: return False
    return True

# 내 코드
# def powerset(idx, si, n, mtx):
#     global flag
#     if flag: return
#     if idx == n:
#         if test(mtx):
#             flag = True
#         return
#     for ni in range(si, D):
#         tmp = mtx[ni]
#         mtx[ni] = [1] * W
#         powerset(idx+1, ni+1, n, mtx)
#         mtx[ni] = [0] * W
#         powerset(idx+1, ni+1, n, mtx)
#         mtx[ni] = tmp

# 선생님 코드
# 이전 재귀 단계에서 n까지 도달해서 true를 반환했으면 계속 true를 반환해서 재귀를 끝낼 수 있도록
# 이렇게 작성하면 굳이 flag를 쓰지 않아도 됨
def powerset(idx, si, n, mtx):
    if idx == n:
        return test(mtx)
    for ni in range(si, D):
        tmp = mtx[ni]
        mtx[ni] = [1] * W
        if powerset(idx+1, ni+1, n, mtx): return True
        mtx[ni] = [0] * W
        if powerset(idx+1, ni+1, n, mtx): return True
        mtx[ni] = tmp
    return False


t = int(input())
for tc in range(1, t+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    if test(arr):
        print(f'#{tc} 0')
    else:
        flag = False
        for n in range(1, K+1):
            meds = []
            if powerset(0, 0, n, arr):
                print(f'#{tc} {n}')
                break


    # 설명
    # 1. 배열 복사
    # - 한 부분이 바뀌고 그 부분만 되돌리면 되면 굳이 배열 복사를 할 필요가 없다.
    # - 배열 복사는 한 부분이 바뀌었을 때 다른 부분이 연쇄적으로 바뀌고 어떻게 되돌릴 지 모를 때 쓰는 것!
    # 2. 기타 가지치기
    # - 여기서 k개 이상이면 통과임 -> 즉, 약품을 k번 투입하면 무조건 통과한다는 것이므로
    # - line 44에서 D까지 볼 필요 없고 k까지만 보면 됨


