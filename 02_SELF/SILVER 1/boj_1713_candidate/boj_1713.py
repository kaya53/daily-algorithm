import sys

sys.stdin = open('input.txt')

# input
N = int(input())
M = int(input())
arr = list(map(int, input().split()))

recom = [1001]*101
pics = []

for stu_num in arr:  # 주어진 추천받은 학생들 순회
    if stu_num in pics:  # 사진틀에 있으면 길이에 상관없이 일단 넣는다
        recom[stu_num] += 1
    else:  # 사진틀에 없으면
        if len(pics) < N:  # 다 차지 않은 경우
            pics.append(stu_num)
            recom[stu_num] = 1
        elif len(pics) == N:  # 다 찬 경우
            min_recom_num = min(recom)

            # min_stu_num = recom.index(min_recom_num)  # 최소 추천을 받은 학생 번호
            # 최소 추천을 받은 학생 중 가장 오래된 애 찾기
            for pic in pics:
                if recom[pic] == min_recom_num:
                    min_stu_num = pic
                    break

            for i in range(N):
                if pics[i] == min_stu_num:  # 최소 득표수 학생을 뺀다
                    pics.pop(i)
                    break  # 한 명 뺐으면 끝
            recom[min_stu_num] = 1001  # 뺀 학생의 추천수 초기화

            # 새로운 학생 넣기
            pics.append(stu_num)
            recom[stu_num] = 1

print(*sorted(pics))
