# 소요시간 10분 pypy 116ms, python 44ms
# 아주 약간 머리를 써야 함
# 빈 row, col이 겹쳐지는 부분에 경비원을 배치하면 되므로
# 빈 row, col 수 중 최대값이 답이 된다
import sys

sys.stdin = open('input.txt')


def solution():
    n, m = map(int, input().split())
    row = [0] * n
    col = [0] * m

    empty_row = n
    empty_col = m
    for i in range(n):
        inp = list(input())
        for j in range(m):
            if inp[j] == 'X':
                if not row[i]:
                    row[i] = 1
                    empty_row -= 1
                if not col[j]:
                    col[j] = 1
                    empty_col -= 1

    return max(empty_row, empty_col)


# for _ in range(3):
print(solution())