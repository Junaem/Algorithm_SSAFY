import sys

sys.stdin = open('input.txt')

def calc(charges, visits):
    dp = [0] * 13
    for month in range(1, 13):
        cheapest = visits[month] * charges[0]
        cheapest = charges[1] if charges[1] < cheapest else cheapest
        dp[month] = dp[month-1] + cheapest

        thr_mon_ago = month - 3 if month - 3 > 0 else 0
        if dp[month] > dp[thr_mon_ago] + charges[2]:
            dp[month] = dp[thr_mon_ago] + charges[2]
    dp[12] = charges[3] if charges[3] < dp[12] else dp [12]

    return dp[12]

T = int(input())
for tc in range(1, T+1):
    charges = list(map(int, input().split()))
    visits = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, calc(charges, visits)))