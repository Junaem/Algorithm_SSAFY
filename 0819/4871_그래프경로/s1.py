import sys

sys.stdin = open('input.txt')

def graph(v, e):
    node = [[False for _ in range(v+1)] for _ in range(v+1)] # [a][b]는 a에서 b로 갈 수 있는지를 표시
    visit = [False for _ in range(v+1)] # 방문한 node를 표시

    def explore(a, g): # a에서 goal을 찾아나가는 여정
        for dest in range(v + 1):
            if node[a][dest] and not visit[dest]: # a가 dest에 갈 수 있고 dest를 가본 적이 없을때
                if dest == g: # dest가 g라면 탐색 성공
                    return 1
                # 그렇지 않으면
                visit[dest] = True # 방문 표시를 한 뒤에
                if explore(dest, g): # dest에서 다시 탐색
                    return 1 # 탐색에 실패하면 return하지 않고, 성공일 경우에만 리턴한다.
                visit[dest] = False # 갔다온 뒤에는 다시 방문표시를 지운다.(이 문제에서는 없어도 될 듯 하다.)
        return 0


    for i in range(e):
        a, b = map(int, input().split())
        node[a][b] = True

    s, g = map(int, input().split())
    return explore(s, g)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    print('#{} {}'.format(tc, graph(V, E)))