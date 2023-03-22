# 퀸의 이동 방향: 가로 세로 대각선 모두 가능; 칸 수 제한 X
# input 8, output: 92

def check(ci, cj):
    for k in range(4):
        si, sj = ci, cj
        while True:
            si += di[k][0]
            sj += di[k][1]
            if si < 0 or si >= n or sj < 0 or sj >= n: break
            if arr[si][sj] == 2: return False
    return True


def queen(idx):
    global res_cnt
    if idx == n:
        res_cnt += 1
        return

    for j in range(n):
        # 같은 열을 이미 방문했다면 continue
        if vj[j]: continue
        # 대각선 내에 말이 있다면 continue
        # 대각선도 행, 열 처럼 배열을 만들어서 처리할 수 있을 것 같다.
        if not check(idx, j): continue
        # 켜기
        arr[idx][j] = 2
        vj[j] = 1
        # 그 다음 퀸 고르러
        queen(idx + 1)
        # 끄기
        arr[idx][j] = 0
        vj[j] = 0


di = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
n = int(input())  # 체크 칸 수;
arr = [[0] * n for _ in range(n)]
vj = [0] * n
res_cnt = 0
queen(0)
print(res_cnt)