def solution(topping):
    answer = 0
    n = len(topping)

    memo1 = [0] * n
    piece1 = set()
    memo1[0] = 1
    piece1.add(topping[0])
    for i in range(1, n):
        if topping[i] not in piece1:
            memo1[i] = memo1[i - 1] + 1
            piece1.add(topping[i])
        else:
            memo1[i] = memo1[i - 1]
    # print('1', memo1)
    # 반대로
    memo2 = [0] * n
    piece2 = set()
    memo2[n - 1] = 1
    piece2.add(topping[n - 1])
    for j in range(n - 2, -1, -1):
        if topping[j] not in piece2:
            memo2[j] = memo2[j + 1] + 1
            piece2.add(topping[j])
        else:
            memo2[j] = memo2[j + 1]
    # print('2', memo2)

    for k in range(n - 1):
        if memo1[k] == memo2[k + 1]:
            answer += 1

    return answer