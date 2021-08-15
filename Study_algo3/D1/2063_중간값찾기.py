import sys

sys.stdin = open('2063.txt')


def mid_num(N, li):
    cnt_li = [0] * 199 # 각 숫자가 몇 개씩 있는지 저장할 리스트

    for i in li: # 인풋 리스트를 돌며 요소를 인덱스로 사용하여 각 숫자의 개수를 센다.
        cnt_li[i] += 1
    cnt = 0 # cnt로 숫자를 세다가 N / 2 보다 크면 멈출 것이다.
    for i in range(200):
        cnt += cnt_li[i]
        if cnt > N / 2 :
            print(i)
            return


N = int(input())
li = list(map(int, input().split()))
mid_num(N, li)
# print(sorted(li)[N//2]) 내장함수를 사용하는 경우