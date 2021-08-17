import sys

sys.stdin = open('input.txt')
# 달들을 미리 정리한다.
mon = [0] * 13
for i in range(1, 13):
    if i <= 7: # 7월까지는 홀수 달이 31일
        mon[i] = 30 + i%2
    else : # 이후에는 짝수 달이 31일
        mon[i] = 30 + (i+1)%2
mon[2] = 28 # 2월은 따로 처리


def date_calc(m1, d1, m2, d2):
    rtn = d2 - d1 # 일수는 일단 빼서 양수든 음수든 만들어 놓는다.
    for m in range(m1, m2): # 두 날짜 사이에 끼어있는 달들의 일 수를 더한다.
        rtn += mon[m]
    return rtn + 1


T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    print('#{} {}'.format(tc, date_calc(m1, d1, m2, d2)))