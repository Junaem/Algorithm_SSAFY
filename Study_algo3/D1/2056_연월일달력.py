import sys

sys.stdin = open('2056.txt')

def is_date(date):
    year = date[:4] # 무조건 8자리가 주어지므로 년도는 검사하지 않는다.
    mon = int(date[4:6]) # 달은 검사를 위해 int
    day = int(date[6:]) # 날짜도 마찬가지

    if mon == 2: # 가장 특이 케이스인 2월부터 처리
        if 1 <= day <= 28: # 직관성을 위해 '<=' 활용
            return '/'.join([year, date[4:6], date[6:]])
    elif 1 <= mon <= 7: # 홀수 달이 31일인 7월까지
        if 1 <= day <= 30 + mon % 2: # 홀수인 경우에만 31일도 되도록 처리
            return '/'.join([year, date[4:6], date[6:]])
    elif 8 <= mon <= 12: # 짝수 달이 31일인 8월 부터
        if 1 <= day <= 30 + (mon+1) % 2: # 짝수일 때만 31일도 포함
            return '/'.join([year, date[4:6], date[6:]])
    return -1 # 다 실패하면 -1 반환


T = int(input())

for tc in range(1, T+1):
    date = input()
    print('#{} {}'.format(tc, is_date(date)))