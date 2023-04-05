import sys
sys.stdin = open('input.txt')


def move(r_no, rnd):
    ci, cj, cd = robot_info[r_no]
    now_order = robot_orders[r_no][rnd % len(robot_orders[r_no])]

    if not now_order:
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            robot_info[r_no][2] = (cd+1) % 4  # 방향 전환
            # move_ls.append([(ci, cj), (ci, cj)])
            move_dict[r_no] = [(ci, cj), (ci, cj)]
        else:
            robot_info[r_no][:2] = [ni, nj]  # 1칸 전진
            move_dict[r_no] = [(ci, cj), (ni, nj)]

    elif now_order == 1:
        robot_info[r_no][2] = (cd+1) % 4
        move_dict[r_no] = [(ci, cj), (ci, cj)]

    elif now_order == 2:
        robot_info[r_no][2] = (cd+2) % 4
        move_dict[r_no] = [(ci, cj), (ci, cj)]

    elif now_order == 3:
        robot_info[r_no][2] = (cd - 1) % 4
        move_dict[r_no] = [(ci, cj), (ci, cj)]

    # 배터리가 방전되면 파괴되는 게 아니므로 살아남은 로봇으로 계속 세어주어야 함
    # 이동만 하지 않도록 처리해주면 됨
    battery[r_no] -= 1 

    # 이동하면서도 파괴가 되었나 봐주어야 하고, 모든 로봇이 다 이동한 후에도 파괴될 것이 있나 봐주어야 함
    # check_destory()


# 교차 확인
def check_cross(move_dict):
    # print(move_dict)
    cross = set()
    for me in move_dict:
        for you in move_dict:
            if me == you: continue
            if move_dict[me] == move_dict[you][::-1]:
                cross.add(me)
                cross.add(you)
    for c_no in cross:
        battery[c_no] = 0
        robot_info[c_no] = robot_orders[c_no] = []


# 이동 후 같은 자리인 경우
# 파괴될 것이 있나 보기
def check_destory():
    destroy_ls = set()
    for me in range(M):
        if not robot_info[me]: continue
        mi, mj = robot_info[me][:2]
        for you in range(M):
            if me == you: continue
            if not robot_info[you]: continue
            yi, yj = robot_info[you][:2]
            if (mi, mj) == (yi, yj):
                destroy_ls.add(me)
                destroy_ls.add(you)

    for d_no in destroy_ls:  # 파괴된 애들은 움직여도 안되니까 배터리도 방전 처리
        battery[d_no] = 0
        robot_info[d_no] = robot_orders[d_no] = []


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    robot_info = [[] for _ in range(M)]
    robot_orders = [[] for _ in range(M)]
    battery = [0] * M
    for e in range(M):
        inp = list(map(int, input().split()))
        robot_info[e] = inp[:3]
        battery[e] = inp[3]
        robot_orders[e] = inp[5:]

    # 명령 늘리기-> 여기서 늘려주기 때문에 C값은 사용 안함
    # 0: 직진, 1: 오른쪽 90도, 2: 180도, 3: 왼쪽 90도
    for ee in range(M):
        rorder = robot_orders[ee]
        tmp = []
        for ro in range(len(rorder)):
            if ro % 2:
                tmp.append(rorder[ro])
            else:
                tmp += [0] * rorder[ro]
        robot_orders[ee] = tmp

    # k초 동안 움직이기
    score = 0
    for rnd in range(K):
        move_dict = {}  # 로봇 번호 : [움직이기 전 좌표, 움직인 후 좌표]
        for rob_no in range(M):
            # 1칸 움직이기; 방전 안된 애들
            if battery[rob_no]:
                # print(rob_no)
                move(rob_no, rnd)
        check_cross(move_dict)
        check_destory()
        # 점수 계산; 파괴 안된 애들은 다 더해주기(방전된 애들도 포함)
        for r in range(M):
            if robot_info[r]:
                score += (r+1)
    print(f'#{tc} {score}')