### coding_style.py

# 1. and, or 조건을 사용할 때는 괄호를 사용한다
#   (condtion1) and (condition2)
#   올바른 예)
#    if (cnt == 5) and (check_data != target_num):
#        return i+1,j+1
#
#    if (l[i][j] == 1) or (l[i][j] == 2):
#        pass
#
#   좋지 않은 예)
#   if (cnt == 5 and check_data!=target_num): return i+1,j+1


# 2. 이름은 global, local이 같지 않도록 하는 것이 좋다
#    함수 이름, local variable 이름 : 같아도 오류는 없음, 하지만 쓰지말자
#    위의 경우 함수 내부에서 자신을 호출하는 재귀 호출을 못함
#    좋지 않은 예)
#    def cnt(color, i, j):
#        cnt = 1

# 3. 불필요한 elif, else 를 사용하지 말자자
#    if ~ else 구조가 좋은지, if ~ 구조가 좋은지 !

#    if (0 <= ni < 19) and (0 <= nj < 19):
#        if board[ni][nj] != color: break
#        else:
#            cnt += 1
#            ci, cj = ni, nj

#    if (0 <= ni < 19) and (0 <= nj < 19):
#        if board[ni][nj] != color: break
#        cnt += 1
#        ci, cj = ni, nj


# 4. try ~ except 는 try 블럭에서 에러 있는 경우 except에 있는 것 수행
# try:
#     before = board[x - i][y - j]
# except:
#     before = 0

# 5. for 문이 중첩된 경우 모든 for문 탈출이 필요하다면, 함수로 분리한다.
# 나쁜예)
# flag_i = False
# flag_j = False
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             if "condition":
#                 flag_j = True
#                 break
#         if flag_j:
#             flag_i = True
#             break
#     if flag_i:
#         break

# 좋은 예)
# def func():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 if "condition":
#                     return "value"

