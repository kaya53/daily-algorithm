def solution(cards):
    # answer = 0
    cards = [0] + cards
    n = len(cards)
    size = [0]
    visited = [0] * n
    for start in range(1, n):
        if visited[start]: continue
        # print('start', start)
        visited[start] = 1
        curr = cards[start]
        cnt = 1
        while not visited[curr]:
            # print(curr)
            visited[curr] = 1
            curr = cards[curr]
            cnt += 1
        size.append(cnt)

    size.sort(reverse=True)
    return size[0] * size[1]