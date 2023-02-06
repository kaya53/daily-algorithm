# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1838

# 회전초밥

# k개에 포함된 초밥의 종류(가짓수)를 구하라
belt = [1, 3, 2, 5, 7, 8, 2, 4, 7, 9]
N = 9 # 초밥의 가짓수
cnt = [0] * (N+1)

print(sorted(belt))
c_cnt = 0
for x in belt:
    if cnt[x] == 0:
        c_cnt += 1
    cnt[x] += 1

print(cnt, c_cnt)

# 슬라이딩 윈도는??
# 회전은 ??