answer = int(1e9)


def backtrack(n, m, cnt, flipped, target):
    global answer
    if cnt > answer: return
    if flipped == target:
        if answer > cnt:
            answer = cnt
        return
    # 행 뒤집기
    for i in range(n):
        for j in range(m):
            flipped[i][j] ^= 1
        # print('행', i)
        backtrack(n, m, cnt + 1, [f for f in flipped], target)
        for j in range(m):
            flipped[i][j] ^= 1
    # 열 뒤집기
    for j in range(m):
        for i in range(n):
            flipped[i][j] ^= 1
        backtrack(n, m, cnt + 1, [f for f in flipped], target)
        for i in range(n):
            flipped[i][j] ^= 1


def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    backtrack(n, m, 0, beginning, target)
    return answer


arr = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
t = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
solution(arr, t)