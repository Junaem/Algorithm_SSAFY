import sys

sys.stdin = open('input.txt')
# 작동 속도를 위해서 문자열을 만든 후 회문인지 확인하지 않고, 회문을 만들면서 틀리면 멈췄다.
def palin():
    li = [input() for _ in range(100)]
    max_len = 1
    for i in range(100): # 고정 축
        for j in range(100): # 검사축 시작점
            # j + max_len 이 100보다 크다는 건 j로는 max보다 큰 값을 만들 수 없다는 것
            if j + max_len < 100:
                for k in range(99, j + max_len -1, -1): # 이 range가 포인트
                    # 가로로 회문을 만들면서 동시에 확인하는 while문
                    a, b = j, k
                    while a < b:
                        if li[i][a] != li[i][b]:
                            break # 회문이 아니다 싶으면 바로 다음 작업으로 간다.
                        a += 1
                        b -= 1
                    else : # max값을 저장
                        if max_len < k - j + 1:
                            max_len = k - j + 1
                    # 세로로 같은 작업을 반복복
                    a, b = j, k
                    while a < b:
                        if li[a][i] != li[b][i]:
                            break
                        a += 1
                        b -= 1
                    else:
                        if max_len < k - j + 1:
                            max_len = k - j + 1
    return max_len




for _ in range(10):
    tc = int(input())
    print('#{} {}'.format(tc, palin()))