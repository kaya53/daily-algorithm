import sys

sys.stdin = open('input.txt')


# 입력
K, S, N = input().split()  # k,s는 문자열, n은 정수임
N = int(N)
arr = [input() for _ in range(N)]  # n번 움직이는 방향

# 초기화
look_up = {'R' : (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
           'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1,1), 'LB': (1, -1)}
chess = [[0] * 8 for _ in range(8)]  # 기본 체스판
# 체스판에 킹이랑 돌 올리기 - 알파벳이 소문자일 수도 있으니 upper 하기
# 킹은 1, 돌은 2로 표시
k_row = 8 - int(K[1])
s_row = 8 - int(S[1])
k_col = ord(K[0].upper()) - 65
s_col = ord(S[0].upper()) - 65
# print(k_col,k_row,s_col,s_row)
chess[k_row][k_col] = 1
chess[s_row][s_col] = 2

# 말 움직이기
ci, cj = k_row, k_col
for dir in arr:
    # 움직일 방향
    dir_i = look_up[dir][0]
    dir_j = look_up[dir][1]
    # 움직인 방향
    ni = ci + dir_i
    nj = cj + dir_j

    # 움직인 방향이 idx 내부이면
    if (0 <= ni <= 7) and (0 <= nj <= 7):
        # 돌이 움직인 방향에 있으면
        if chess[ni][nj] == 2:
            if (0 <= ni+dir_i <= 7) and (0 <= nj+dir_j <= 7):
                chess[ni+dir_i][nj+dir_j] = 2  # 여기서 인덱스가 벗어나도 continue를 해야 함
            else: continue  # 돌의 다음이 인덱스 밖이면 continue
        chess[ni][nj] = 1
        chess[ci][cj] = 0
        ci, cj = ni, nj
    else:  # 인덱스 밖이면 다음 반복으로
        continue


res = [None, None]
# 위치 변환
for i in range(8):
    for j in range(8):
        if chess[i][j] == 1:
            res_ki = chr(j + 65)
            res_kj = str(8 - i)
        if chess[i][j] == 2:
            res_si = chr(j + 65)
            res_sj = str(8 - i)


print(res_ki+res_kj, res_si+res_sj, sep='\n')