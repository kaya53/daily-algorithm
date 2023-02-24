import sys

sys.stdin = open('sample_input.txt')

# 주어진 방향 조합을 가지고 프로세서를 찾는 함수
def find_processor(choice, arr, pcnt):
    global mmin
    # choice : 각 프로세서의 방향이 담긴 배열
    # choice[i], processor[i]: 시작점
    # 중간에 가다가 프로세서가 있거나, 다른 선이 있으면 리턴
    for k in range(lenP):
        d = choice[k]
        si, sj = processor[k]
        while True:
            ni, nj = si + dir[d][0], sj + dir[d][1]
            if ni < 0 or ni >= n or nj < 0 or nj >= n: break  # 인덱스 밖으로 나갔다면 break
            if arr[ni][nj]:
                return 0 # 그 다음 칸에 전선이나 프로세서가 있는 경우
            # 인덱스 밖도 아니고, 전선이나 프로세서도 없다면
            arr[ni][nj] = 1
            pcnt += 1
            si, sj = ni, nj
    if pcnt and mmin > pcnt:
        mmin = pcnt
    return


def choose(idx, k):
    global cnt
    if idx == lenP:
        cnt += 1
        find_processor(choice, [i[:] for i in arr], 0)
        return

    for k in range(4):
        choice[idx] = k
        choose(idx + 1, k)
        choice[idx] = 0


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    mmin = int(1e9)
    processor = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:
                processor.append((i, j))
    lenP = len(processor)
    choice = [0] * lenP
    choose(0, 0)
    print(f'#{tc} {mmin}')

