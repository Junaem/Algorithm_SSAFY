import sys

sys.stdin = open('input.txt')


def rsp(A, B): # 번호를 받아 그 사람의 카드를 찾고, 가위바위보를 실행
    a = cards[A]
    b = cards[B]

    if a == b:
        return A
    elif a == 1 and b == 3:
        return A
    elif a == 3 and b == 1:
        return B
    elif a > b:
        return A
    else:
        return B

def devide(li): # 토너먼트 조를 짜고 가위바위보를 시키는 함수
    half = len(li)//2 + len(li)%2 # 홀수일 때는 절반에 +1
    if len(li) > 1: # 길이가 2 이상일때
        lft = devide(li[:half]) # 왼쪽 절반에 재귀
        rgt = devide(li[half:]) # 오른쪽 절반 재귀
        winner = rsp(lft, rgt) # 나온애들 가위바위보해서 이긴 친구 리턴
    else:
        winner = li.pop() # 혼자밖에 없으면 그냥 승자
    return winner


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [] # [1,2,3,4,5,6]
    for i in range(1, N+1): # 참가자들의 번호를 기억(ex.[1,2,3,4]
        num.append(i)
    full_li = list(map(int, input().split())) # 입력을 받아서
    cards = {}
    for i in range(N): # 입력을 딕셔너리에 저장
        cards[i + 1] = full_li[i] # {1: 가위 , 2: 바위}
    print('#{} {}'.format(tc, devide(num)))
