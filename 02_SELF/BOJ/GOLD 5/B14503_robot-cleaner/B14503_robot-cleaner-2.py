import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(ci, cj, cd):
    # 현재 칸의 주변 4칸 중 청소가 된 칸이 있는 지 없는지
    for _ in range(4):
        cd = (cd - 1) % 4
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if not arr[ni][nj]:  # 청소 가능
            return ni, nj, cd
    # 청소 가능한 칸 없음
    # 어차피 1바퀴 돌았으니까 cd는 처음 값과 같음
    bi, bj = ci - delta[cd][0], cj - delta[cd][1]
    if arr[bi][bj] != 1:  # 후진 가능; 청소 했거나, 빈 칸
        return bi, bj, cd
    # 후진 불가
    return False


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
ri, rj, rd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    # 1번
    if not arr[ri][rj]:
        cnt += 1
        arr[ri][rj] = -1

    # 2, 3번
    flag = check(ri, rj, rd)
    if flag is not False:
        ri, rj, rd = flag
    else:
        break

print(cnt)