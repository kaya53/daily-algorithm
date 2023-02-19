import sys

sys.stdin = open('input.txt')

n, k = map(int, input().split())  # 컨베이어 길이, 내구도가 0인 칸의 개수
belt = [[0, 0] for _ in range(2*n)]
i = 0
for num in map(int, input().split()):
    belt[i][0] = num
    i += 1
# print(belt)  # [[1, 0], [2, 0], [1, 0], [2, 0], [1, 0], [2, 0]]

stage = 0
while True:
    stage += 1
    # 1. 벨트가 로봇과 함께 한 칸씩 옆으로 간다.
    belt = [belt[-1]] + belt[:2*n-1]
    for x in range(2*n-1, -1, -1):
        if belt[x][1] == 1: # 로봇이 있으면
            if x == n-1:
                belt[x][1] = 0  # n번째 칸에 로봇이 있으면 하차
                continue
            # if belt[x][0] >= 1: belt[x][0] -= 1  # 내구도 감소

    # print(belt)
    # 2. 로봇이 있는데, 로봇이 이동할 수 있다면 먼저 올라간 로봇부터 이동한다. -- 역순으로 이동
        # 2-1. 로봇 이동 조건: 이동하려는 칸에 로봇 없음 + 내구도 1이상인 칸
    for i in range(2*n-1, -1, -1):
        if i == 2*n -1:
            i = -1
        if belt[i][1] and not belt[i+1][1] and belt[i+1][0] >= 1:  # 이동 가능하다면
            if i == n-2:
                belt[i][1] = 0  # 로봇 하차
                belt[i+1][0] -= 1 # 내구도 감소
                continue
            belt[i+1][1] = 1  # 로봇 이동
            belt[i+1][0] -= 1  # 내구도 1 감소
            belt[i][1] = 0  # 원래 위치에서 로봇 초기화
    # 3. 올리는 위치의 내구도가 0이 아니면 로봇을 올린다.
    if belt[0][0] != 0:
        belt[0][1] = 1
        belt[0][0] -= 1  # 로봇이 올라왔으니 내구도 감소
    # 4. 내구도가 0인 칸의 개수가 k개 이상이면 종료 or back to 1
    zero_cnt = 0
    for j in range(2*n):
        if belt[j][0] == 0:
            zero_cnt += 1
    if zero_cnt >= k:
        break
print(stage)

# belt = [[0]*n for _ in range(2)]
#for idx, elem in enumerate(list(map(int, input().split()))):
    # if idx < n:  # 첫째줄
        # belt[0][idx] = elem
    #else:
        #idx = (n*2 - 1) - idx
        #belt[1][idx] = elem
# print(belt)


