### 5789 현주의 상자 바꾸기

# test_case 6의 경우 덮어쓰기가 많이 발생한다
# 덮어쓰기를 안하고 싶다면?  덜하고 싶다면? => 코드를 어떻게 변경해야 할까?

def code_01():
    t = int(input())

    for num in range(1, t+1):
        n, q = map(int, input().split())
        box = [0] * n #[0 for _ in range(n)]

        for i in range(1, q+1):
            l, r = map(int, input().split())

            for idx in range(l-1, r):
                box[idx] = i

        print(f'#{num}', ' '.join(map(str, box)))


def code_02():
    T = int(input())
    # range(1, T+1)
    for t in range(T):
        N, Q = map(int, input().split())
        box = [0] * N
        # range(1, Q+1)
        for i in range(Q):
            L, R = map(int, input().split())
            # range(L-1, R)
            for x in range(L, R + 1):
                box[x - 1] = i + 1   # box[x] = i

        box = ' '.join(map(str, box))
        # print(f'#{t} {box}')
        print(f'#{t + 1} {box}')


def code_03():
    def solve(T):
        for test_case in range(1, T + 1):
            N, Q = map(int, input().rstrip().split())
            box = [0] * N
            for i in range(1, Q + 1):
                L, R = map(int, input().rstrip().split())
                s_idx = L - 1
                e_idx = R
                box[s_idx:e_idx] = [i] * (e_idx - s_idx)
            print(f'#{test_case} {" ".join(map(str, box))}')

    def input_output():
        T = int(input().rstrip())
        return solve(T)

    input_output()


def code_03_after():
    def solve(N, LR_list):
        box = [0] * N
        for i, (L, R) in enumerate(LR_list, start=1):
            s_idx = L - 1
            e_idx = R
            box[s_idx:e_idx] = [i] * (e_idx - s_idx)
        return box

    def input_output():
        T = int(input().rstrip())
        for test_case in range(1, T + 1):
            N, Q = map(int, input().rstrip().split())
            LR_list = [map(int, input().rstrip().split()) for _ in range(Q)]

            box = solve(N, LR_list)

            print(f'#{test_case} {" ".join(map(str, box))}')
        return

    input_output()


# 두 개 파일의 내용이 같은지 비교하는 함수
def PassFail(prefix):
    afile = prefix + 'output.txt'
    bfile = prefix + 'my_output.txt'
    infile = prefix + 'input.txt'

    with open(infile, 'r') as t:
        T = int(t.readline())

    with open(afile, 'r') as a, open(bfile, 'r') as b:
        for x in range(T):
            if a.readline().strip() != b.readline().strip():
                return 'Fail'
        return 'Pass'

        #return 'Fail' if a.read().strip() != b.read().strip() else 'Pass'

        #A = a.readline()  # '첫 번째줄\n'
        #A = a.read()  # 전체 파일을 한 개 문자열로 가져옴
        #AA = [A]  # 문자열의 escape sequence를 실행하지 않고 그대로 보려고 리스트로 만듦
        #B = b.readlines()  # [ '첫 번째줄\n', '두 번째줄\n' ,,,'마지막줄\n']

        #print(A, AA, B, sep='\n')

import sys
prefix = '04_5789_'
# stdout_temp = sys.stdout
# sys.stdout = open(prefix + 'my_output.txt', 'w')
stdin_temp = sys.stdin
sys.stdin = open(prefix + 'input.txt', 'r')

# 이것이 실행할 코드
code_03_after()

sys.stdin.close()
sys.stdin = stdin_temp
# sys.stdout.close()
# sys.stdout = stdout_temp

# 채점 코드
# result = PassFail(prefix)
# print(f'Result = {result}')


