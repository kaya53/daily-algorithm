# 소요시간 52분 (11:57 ~ 12:49)
# - 숨어 있는 조건을 생각해내는 것이 까다로웠다
# => 한 글자를 더하고 빼고 바꾸고를 어떻게 코드로 구현할 건지에 대한 문제
# - 무작정 두 글자 사이의 차를 더하면 한 글자에서 2개가 차이나고 한 글자에서 3개가 차이나서
# 그걸 더하면 1개가 차이난다고 인식하기 때문에 이렇게 하면 안된다
# - 그래서 변수를 3개를 사용했다.
# 1. flag: 한 변수에서 두 글자 이상 차이나면 바로 false
# 2. plus_flag: 기준 단어의 문자 수가 비교 단어 문자 수 보다 많은 경우
# 3. minus_flag: 기준 단어의 문자 수가 비교 단어 문자 수 보다 적은 경우
# => 2, 3을 더해서 0이나 1이 되면 조건에 충족하지만 둘 중 하나라도 1보다 크면 조건 미충족
import sys

sys.stdin = open('input.txt')


def get_cnt_ls(target_str):
    cnt_ls = [0] * 26
    for c in target_str: cnt_ls[ord(c)-65] += 1
    return cnt_ls


N = int(input())
STD = input()
words = [input() for _ in range(N-1)]

std_cnt = get_cnt_ls(STD)

res_cnt = 0
for word in words:
    flag = True
    plus_flag = minus_flag = 0
    word_cnt = get_cnt_ls(word)

    for i in range(26):
        k = std_cnt[i] - word_cnt[i]
        if k > 1 or k < -1:
            flag = False
            break
        elif k == 1: plus_flag += 1
        elif k == -1: minus_flag += 1

    if flag and (plus_flag <= 1 and minus_flag <= 1): res_cnt += 1
    
print(res_cnt)