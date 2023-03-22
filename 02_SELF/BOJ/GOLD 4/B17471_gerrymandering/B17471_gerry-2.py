import sys

sys.stdin = open('input.txt')


def connected(si, area, connect, selected, num):
    lenA = len(area)
    if lenA == 1:  # 길이가 1이면 무조건 연결되어 있는 것이니까
        return True
    if lenA == n or not lenA:  # 전체 다 들어오면 건너뛰기
        return False

    connect[area[0]] = 1
    x = infos[si]
    for ni in infos[si]:
        if selected[ni] == num and not connect[ni]:
            connect[ni] = 1
            connected(ni, area, connect, selected, num)

    if sum(connect) == lenA:
        return True
    return False


def count_population(area1, area2):
    cnt1 = cnt2 = 0
    for elem1 in area1:
        cnt1 += population[elem1]
    for elem2 in area2:
        cnt2 += population[elem2]
    return abs(cnt1 - cnt2)


def subset(idx):
    global min_res

    if idx == n:
        # print(selected)
        # 여기서 selected가 연결이 되어 있으면 그 배열을 가지고
        # 다른 아이들도 연결이 되어 있는 지 판별하기
        area1 = []
        for i, elem in enumerate(selected):
            if elem:
                area1.append(numbers[i])
        area2 = list(set(numbers) - set(area1))
        res1 = res2 = 0
        if area1:
            res1 = connected(area1[0], area1, [0] * (n + 1), [0] + selected, 1)
        if res1:
            res2 = connected(area2[0], area2, [0] * (n + 1), [0] + selected, 0)

        if res1 and res2:
            # 인구 차이 구하기
            # print(area1, area2)
            tot = count_population(area1, area2)
            if min_res > tot:
                min_res = tot
        return
    selected[idx] = 1
    subset(idx+1)
    selected[idx] = 0
    subset(idx+1)


# for _ in range(4):
n = int(input())  # 구역의 개수
population = [0] + list(map(int, input().split()))  # 각 구역 인구; 1번 부터 세기 위해
infos = [0] + [list(map(int, input().split()))[1:] for _ in range(n)]
min_res = float('inf')

numbers = list(range(1, n+1))
selected = [0] * n
subset(0)

if min_res != float('inf'):
    print(min_res)
else:
    print(-1)