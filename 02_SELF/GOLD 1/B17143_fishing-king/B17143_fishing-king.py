import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

def move_shark(shark_no):

    cr, cc, s, d, size = infos[shark_no]

    move = 0  # 상어가 몇 칸 움직였는 지 셀 변수
    while move < s:
        nr, nc = cr + delta[d][0], cc + delta[d][1]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            nr, nc = cr + delta[oppo[d]][0], cc + delta[oppo[d]][1]
            cr, cc = nr, nc
            move += 1
            d = oppo[d]
            continue
        cr, cc = nr, nc
        move += 1

    infos[shark_no] = [cr, cc, s, d, size]
    if merge_sh.get((cr, cc)):
        tmp = merge_sh[(cr, cc)]
        # print(tmp)
        tmp.append((shark_no, infos[shark_no][4]))
        merge_sh[(cr, cc)] = tmp
    else:
        merge_sh[(cr, cc)] = [(shark_no, infos[shark_no][4])]
        # 움직인 자리에 상어가 있으면
        # if arr[cr][cc]:
        #     if infos[arr[cr][cc]][4] < size:
        #         arr[cr][cc] = shark_no
        #         infos[shark_no] = [cr, cc, s, d, size]
        # else:
        #     arr[cr][cc] = shark_no
        #     infos[shark_no] = [cr, cc, s, d, size]

# for _ in range(4):
R, C, m = map(int, input().split())
# arr = [[[] for _ in range(C)] for _ in range(R)]
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
oppo = {0: 1, 1: 0, 2: 3, 3: 2}
infos = {}

for x in range(1, m+1):
    # 좌표들, 속력, 이동 방향, 상어 크기
    a, b, c, d, e = map(int, input().split())
    infos[x] = [a-1, b-1, c, d-1, e]
    # arr[a-1][b-1] = x  # 좌표에는 상어 번호만

shark = 0
for col in range(C):  # 1초마다 어부의 이동
    # 상어가 있으면 잡기
    min_row = R
    killed = 0
    # print('col', col, )
    for ii in range(1, m+1):
        if infos[ii] and infos[ii][1] == col:
            if min_row > infos[ii][0]:
                min_row = infos[ii][0]
                killed = ii
    if min_row != R:  # 먹을 상어가 존재
        shark += infos[killed][4]
        infos[killed] = 0
        # print('killed', killed)
    # print('infos', infos)
    # for row in range(R):
    #     if arr[row][col] and infos[arr[row][col]]:
    #         no = arr[row][col]
    #         shark += infos[no][4]
    #         infos[no] = 0
    #         arr[row][col] = 0

    # 상어 이동하기
    merge_sh = {}
    for z in range(1, m + 1):
        if infos[z]:
            move_shark(z)
    # print('merge_sh', merge_sh)

    # 상어 여러 마리가 같이 있으면 합치기
    for items in merge_sh.values():
        if len(items) > 1:
            sortt = sorted(items, key=lambda x: (-x[1], x[0]))  # 사이즈가 큰 것 순으로 정렬
            for k in range(1, len(sortt)):  # 큰 애 빼고 나머지는 없애 버리기
                infos[sortt[k][0]] = 0

    # print()

print(shark)