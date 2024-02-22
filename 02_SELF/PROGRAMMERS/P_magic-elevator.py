answer = int(1e9)

def recur(num, tot):
    global answer
    # print(num, tot)
    if num <= 5:
        answer = min(answer, tot + num)
        return
    num, v = divmod(num, 10)
    if v == 5:
        recur(num + 1, tot + 5)
        recur(num, tot + 5)
    elif v > 5:
        recur(num + 1, tot + (10 - v))
    else:
        recur(num, tot + v)


def solution(storey):
    recur(storey, 0)
    return answer