import sys

sys.stdin = open('input.txt')

def rec(rst, cnt):
    global n_max
    leng = len(rst)
    pass_cnt = 0     # 가지치기를 위해 바꿀 필요가 없으면 넘어갔는데, for문을 통째로 넘어갔을때 대처하기 위한 카운트
    if cnt and rst[:cnt] != SRT_NUMS[:cnt]: # cnt번 스왑을 했을때, 최대가 될 가망성이 없을때는 리턴
        return

    if cnt != CHG:
            for i in range(leng - 1):     # i는 마지막 전까지
                if NUMS[i] == SRT_NUMS[i]:  # 만약 i번째 숫자가 제대로된 숫자가 와있으면 바꿀 필요없으니 가지치기
                    pass_cnt += 1
                    continue
                for j in range(i + 1, leng):  # j는 i다음부터 마지막까지
                    rst[i], rst[j] = rst[j], rst[i]
                    rec(rst, cnt + 1)   # 스왑 후 재귀, 다시 스왑 되돌림
                    rst[i], rst[j] = rst[j], rst[i]
    else: # 만약 필요한 만큼 바꿨으면
        n_sum = 0  # 리스트를 숫자로 바꿔주고
        for i in range(leng):
            n_sum += rst[leng -1 -i] * (10**i)

        if n_sum > n_max: # 최대값과 비교
            n_max = n_sum

    if pass_cnt == len(rst)-1:   # 만약 for문을 다 스왑했을때(이미 정렬이 끝났을때)는
        n_max = all_pass(rst, CHG-cnt) # 특별처리
    return n_max

def all_pass(rst, left):
    if left % 2: # 남아있는 카운트가 홀수고
        if len(rst) == len(set(rst)): # 중복되는 숫자가 없을때는
            rst[-1], rst[-2] = rst[-2], rst[-1]  # 한 번만 제일 뒤랑 그 앞을 스왑해준다

    n_sum = 0 # 숫자로 변환하여 리턴
    for i in range(len(rst)):
        n_sum += rst[len(rst) - 1 - i] * (10 ** i)
    return n_sum

T = int(input())
for tc in range(1, T+1):
    NUMS, CHG = input().split()
    NUMS = list(map(int, NUMS))
    SRT_NUMS = sorted(NUMS, reverse=True) # 이상의 최대값
    CHG = int(CHG)
    n_max = 0 # 만들 수 있는 최대값
    print('#{}'.format(tc), rec(NUMS, 0))
