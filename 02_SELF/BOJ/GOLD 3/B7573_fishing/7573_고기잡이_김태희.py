import sys

input = sys.stdin.readline

N,L,M = map(int,input().rstrip().split())
f_list = [list(map(int,input().rstrip().split())) for _ in range(M)]
f_list.sort(key=lambda f: (f[0],f[1]))

def solve():
    res_max = 0
    for i in range(M): # 그물(직사각형 윗변)을 걸칠 기준 물고기
        r,c = f_list[i]
        for h in range(1,L//2): # ㄱ 처럼 가로,세로 각각 한변의 길이로 생각하면 결국 *2 한 값이 그물의 둘레가 됨!
            w = L//2-h  # 높이가 h일때 가능한 너비 w
            for d in range(w+1):
                cnt = 1 # 항상 자신을 걸쳐서 그물은 항상 던질 수 있으므로
                for j in range(i+1, M): #i물고기의 그물 안에 다른  j물고기가 포함될수 있는지 확인
                    o_r, o_c = f_list[j]

                    if o_r> r+h: break
                    if c-d<=o_c and o_c<=c+(w-d): cnt += 1

                if res_max<cnt: res_max = cnt
    
    print(res_max)

solve()