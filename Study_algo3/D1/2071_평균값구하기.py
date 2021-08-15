import sys

sys.stdin = open('2071.txt')

def my_avg(li):
    rtn = 0
    for i in li:
        rtn += i # 리스트의 합을 저장
    rtn = rtn / len(li) # 총합을 전체 갯수로 나눠 평균값 계산
    if rtn - int(rtn) >= 0.5: # 평균값의 소수부가 0.5이상이면
        rtn += 1 # 평균값에 1을 더 한다
    return int(rtn) # 소수부를 버리고 리턴


T = int(input())

for tc in range(1, T+1):
    li = list(map(int, input().split()))
    print('#{} {}'.format(tc, my_avg(li)))