# 230529 python 121ms => 2시간 소요 17:05 ~ 19:17
# 틀린 이유
# 1. find_square에서 in_square 초기화 위치 오류
import sys

sys.stdin = open('input.txt')


def move_people():
    global remain

    moved = [None] * M
    new = {}

    for loc, loc_ls in participants.items():
        ci, cj = loc
        now_dist = abs(ci - exit_loc[0]) + abs(cj - exit_loc[1])
        flag = False
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj]: continue
            next_dist = abs(ni - exit_loc[0]) + abs(nj - exit_loc[1])
            if now_dist > next_dist:  # 이동 가능
                flag = True
                if (ni, nj) == exit_loc:  # 출구 도착
                    remain -= len(loc_ls)
                    for p_no in loc_ls:
                        distance[p_no] += 1
                else:
                    for p_no in loc_ls:
                        moved[p_no] = (ni, nj)
            if flag: break # 이동 가능한 데가 생기면 바로 끝내주기 => 상하 우선이니까
        if flag is False:  # 어디도 이동 못함 => 그대로 new 딕셔너리에 옮겨주기
            new[loc] = loc_ls
            
    for idx, move_loc in enumerate(moved):
        if move_loc is None: continue
        mi, mj = move_loc
        distance[idx] += 1
        if new.get((mi, mj)):
            new[(mi, mj)].append(idx)
        else:
            new[(mi, mj)] = [idx]
    return new


def find_square():
    for size in range(2, N+1):
        for i in range(N):
            for j in range(N):
                flag_parti = flag_exit = False
                in_square = []
                for pi, pj in participants:
                    # print(i, i+size-1, j, j+size-1)
                    if i <= pi <= i + size - 1 and j <= pj <= j + size - 1:
                        flag_parti = True
                        if (pi, pj) not in in_square: in_square.append((pi, pj))
                if i <= exit_loc[0] <= i+size-1 and j <= exit_loc[1] <= j+size-1:
                    flag_exit = True

                if flag_parti and flag_exit: return size, i, j, in_square


def rotate_maze():
    global exit_loc

    size, si, sj, in_square = find_square()
    # print('find square', size, si, sj)
    after = [[0] * N for _ in range(N)]
    new = {}
    # 안돌리는 애들
    for pi, pj in participants:
        if (pi, pj) not in in_square:
            new[(pi, pj)] = participants[(pi, pj)]
    # print('first new', new, in_square)

    is_exit_changed = False
    for ki in range(size):
        for kj in range(size):
            # 출구 돌리기
            if (si+ki, sj+kj) == exit_loc and is_exit_changed is False:
                exit_loc = (si+kj, sj+size-ki-1)
                is_exit_changed = True  # 이거 안해주면 돌아간 후에 출구가 또 돌아갈 수도 있음
            # 참가자 돌리기
            if (si+ki, sj+kj) in in_square:
                new[(si+kj, sj+size-ki-1)] = participants[(si+ki, sj+kj)]
            # 내구도 빼기
            if arr[si+ki][sj+kj] > 0:
                arr[si+ki][sj+kj] -= 1
            after[si+kj][sj+size-ki-1] = arr[si+ki][sj+kj]
    # 원래 배열에 붙이기
    for i in range(si, si+size):
        for j in range(sj, sj+size):
            arr[i][j] = after[i][j]
    return new


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
participants = {}
# 참가자 정보 저장
for no in range(M):
    ii, jj = map(lambda x: int(x)-1, input().split())
    if participants.get((ii, jj)):
        participants[(ii, jj)].append(no)
    else: participants[(ii, jj)] = [no]

exit_loc = tuple(map(lambda x: int(x)-1, input().split()))

distance = [0] * M  # 이거 이렇게 안해주고 그냥 변수로 해놓고 다 더해도 될것 같음
remain = M

for _ in range(K):
    participants = move_people()
    if remain == 0: break
    participants = rotate_maze()

print(sum(distance))
print(exit_loc[0]+1, exit_loc[1]+1)  # 0,0에서 시작하도록 바꿔놨기 때문에
