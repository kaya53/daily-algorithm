# 230531 python 375ms => 1시간 ~ 1시간 30분 소요
# 유의할 점
# 1. 새로 바뀌는 것과 안 바뀌는 것을 어떻게 구분할 지
# - 이동할 때는 다 같이 이동해서 구분하지 않아도 됨
# - 합칠 때는 합칠 대상이 아닌 것도 새 배열에 넣어주는 것을 잊으면 안된다.

# 2. 합친 것을 나누고 이동까지 시키면 안된다
# - 그 다음 턴 시작에서 이동을 하기 때문에 이동이 두 번 이루어짐
import sys

sys.stdin = open('input.txt')


def move_atom():
    new = [[[] for _ in range(N)] for _ in range(N)]

    for ci in range(N):
        for cj in range(N):
            if arr[ci][cj]:
                for m, s, d in arr[ci][cj]:
                    ni = (ci + delta[d][0]*s) % N
                    nj = (cj + delta[d][1]*s) % N
                    new[ni][nj].append((m, s, d))
    # for ne in new:
    #     print(ne)
    return new


def merge_atom(moved_arr):
    new = [[[] for _ in range(N)] for _ in range(N)]
    for ci in range(N):
        for cj in range(N):
            if not moved_arr[ci][cj]: continue
            if len(moved_arr[ci][cj]) == 1: new[ci][cj] = moved_arr[ci][cj]
            else:
                length = tot_m = tot_s = 0
                before_d = (1 if not moved_arr[ci][cj][0][2] % 2 else 2)
                d_flag = True
                for m, s, d in moved_arr[ci][cj]:
                    length += 1
                    tot_m += m
                    tot_s += s
                    if length == 1: continue
                    now_d = (1 if not d % 2 else 2)
                    if before_d != now_d: d_flag = False
                    before_d = now_d

                # print(tot_m//5, tot_s//length, d_flag)
                next_m, next_s = tot_m //5, tot_s // length
                if next_m == 0: continue  # 질량이 0이면 소멸
                
                # 여기서 미리 옮겨놓으면 다음 번 턴에서 이동을 한 번 더 하게 되므로 원래 자리에 넣어놓아야 함
                if d_flag is False:
                    for k1 in [1, 3, 5, 7]:
                        new[ci][cj].append((next_m, next_s, k1))
                else:
                    for k2 in [0, 2, 4, 6]:
                        new[ci][cj].append((next_m, next_s, k2))
    return new


delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# for _ in range(2):
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, x, y, z = map(int, input().split())  # 위치, 질량, 속력, 방향 순
    arr[r-1][c-1].append((x, y, z))

for _ in range(K):
    moved = move_atom()
    # for mo in moved:
    #     print(mo)
    # print()
    arr = merge_atom(moved)

# output
ssum = 0
for a in arr:
    for atoms in a:
        for atom in atoms:
            ssum += atom[0]
print(ssum)