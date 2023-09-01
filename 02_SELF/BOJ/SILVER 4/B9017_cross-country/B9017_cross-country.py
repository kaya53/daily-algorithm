# 소요시간 20분 => 72ms
import sys

sys.stdin = open('input.txt')


def is_six():
    new = []
    board_set = set(board)
    for bs in board_set:
        if board.count(bs) == 6: new.append(bs)
    return new


T = int(input())
for _ in range(T):
    N = int(input())
    board = list(map(int, input().split()))
    # 모두 완주했는 지 추리기
    board_six = is_six()
    dict_six = {}
    for b in board_six: dict_six[b] = []

    score = 0
    for idx, team in enumerate(board):
        if dict_six.get(team, -1) != -1:
            score += 1
            dict_six[team].append(score)

    # 우승팀 구하기
    min_score = 10000
    winner = 0
    for k, v in dict_six.items():
        now_score = sum(v[:4])
        if min_score > now_score:
            min_score = now_score
            winner = k
        elif min_score == now_score:
            if dict_six[winner][4] > v[4]:
                winner = k
    print(winner)
