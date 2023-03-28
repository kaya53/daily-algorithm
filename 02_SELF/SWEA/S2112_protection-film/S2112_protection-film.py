import sys

sys.stdin = open('input.txt')


def test(arr):
    passed = 0
    for j in range(W):
        i = 0
        while i <= D-K:
            ssum = 0
            for ni in range(i, i+K):
                ssum += arr[ni][j]
            if ssum == 0 or ssum == K:
                # print(j)
                passed += 1
                break
            i += 1

    if passed == W: return True
    return False


def comb(idx, ci, n, row, choice):
    if flag: return
    if idx == n:
        portion_in(choice, n, arr)
        return

    for ni in range(ci, row):
        choice[idx] = ni
        comb(idx+1, ni+1, n, row, choice)


def powerset(idx, n, choice):
    if idx == n:
        meds.append(list(choice))
        return
    choice[idx] = 1
    powerset(idx+1, n, choice)
    choice[idx] = 0
    powerset(idx+1, n, choice)


def portion_in(choice, n, arr):
    global flag
    # n: 약품 투입 개수
    for m in range(2**n):  # 약품 조합들을 순회
        mtx = [x[:] for x in arr]
        for e in range(n):
            med = meds[m][e]  # 약품 종류
            mtx[choice[e]] = [med] * W
        # 이 단계에서 성능 검사
        if test(mtx):
            flag = True
            return


t = int(input())
for tc in range(1, t+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    if test(arr):
        print(f'#{tc} 0')
    else:
        flag = False
        for n in range(1, D+1):
            meds = []
            powerset(0, n, [0] * n)
            # print(meds)  # 어떤 약품을 넣을 것인지
            comb(0, 0, n, D, [0] * n)
            if flag:
                print(f'#{tc} {n}')
                break


