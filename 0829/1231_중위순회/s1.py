import sys

sys.stdin = open('input.txt')

def joongwi(nd): # 중위로 도는 재귀함수
    if child[nd]: # 자식이 있으면
        joongwi(child[nd][0]) # 첫번째(왼쪽) 자식으로 재귀
    print(nodes[nd], end='') # 본인 값 출력
    if len(child[nd]) > 1: # 자식이 2 이상이면
        joongwi(child[nd][1]) # 두번째 자식 재귀


for tc in range(1, 11):
    N = int(input())
    nodes = ['' for _ in range(N+1)]
    child = [[] for _ in range(N + 1)]
    for _ in range(N):
        st = list(input().split()) # 한 줄을 받아서
        idx, val, cld = int(st.pop(0)), st.pop(0), list(map(int, st)) # 할당
        nodes[idx] = val # 노드에 값을 넣고
        child[idx] = cld # 자식 리스트에 자식을 넣는다.
    print('#{} '.format(tc), end='')
    joongwi(1)
    print()