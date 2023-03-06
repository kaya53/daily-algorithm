import sys

sys.stdin = open('input.txt')


def get_result(arr):
    # 1. 한 나라의 승, 무, 패 합이 반드시 5 여야 함
    for i in range(6):
        nation = 0
        for j in range(3):
            nation += arr[i][j]
        if nation != 5: return 0
    # 2. 총 이긴 경기 수 = 총 진 경기 수
    whole = 0
    for k in range(6):
        whole += arr[k][0]
        whole -= arr[k][2]
    if whole: return 0
    # 3. 무승부는 대칭 관계여야 함
    draw = 0
    for z in range(6):
        if draw <= 0:
            draw += arr[z][1]
        else:
            draw -= arr[z][1]
    if draw: return 0

    # 1, 2, 3 모두 빠져나가면
    return 1


infos = [[], [], [], []]
for x in range(4):
    inp = list(map(int, input().split()))
    for y in range(0, 16, 3):
        infos[x].append(inp[y:y+3])

res_ls = []
for info in infos:
    ans = get_result(info)
    res_ls.append(ans)

print(' '.join(map(str, res_ls)))