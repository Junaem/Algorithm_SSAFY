import sys

# input을 파일로 받아오기
sys.stdin = open('input.txt')

# 하나의 테스트 케이스를 수행할 함수
def view(bld_num, blds):
    #리턴할 값
    ret = 0
    # i가 가장 높을 경우 위의 2단계를 건너뛰기 위해 while을 썼다.
    i = 2
    while(i< bld_num-2):
        # 주변 2칸 내 가장 높은 건물을 저장할 변수
        highest_neighbor = 0

        # 주변 2칸 중 max인 값을 찾는 for문
        for k in [i-2, i-1, i+1, i+2]:
            if blds[k] > highest_neighbor:
                highest_neighbor = blds[k]
        # 가장 높은 이웃 건물이 현재 탐색중인 건물보다 낮으면 그 차를 리턴할 값에 더한다. 
        if blds[i] > highest_neighbor:
            ret += blds[i] - highest_neighbor
            #옆의 두 집은 확인할 필요가 없으므로 + 3
            i += 3
        else:
            i += 1

    return ret


for i in range(10):
    bld_num = int(input())
    bld_list = list(map(int, input().split()))
    print('#{} {}'.format(i+1, view(bld_num, bld_list)))
