import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    # box의 개수와 행동 실행 횟수
    N, Q = map(int, input().split())
    # index를 편하게 쓰기위해 N+1개의 박스를 만들었다.
    boxes = [0] * (N + 1)

    # i값을 1부터 시작
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        # 인덱스를 통해 박스의 값 변환
        for idx in range(L, R+1):
            boxes[idx] = i
    # 출력 형식에 맞게 str로 변환. join을 쓰니 원인을 알 수 없이 fail이 떠서 직접 구현하여 사용하니 괜찮았다.
    st = ''
    for box in boxes[1:]:
        st += ' ' + str(box)
    print('#{}{}'.format(t, st))
