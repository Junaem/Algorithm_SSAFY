import sys

sys.stdin = open('input.txt')

def graph(n):
    node = [[] for _ in range(100)] # 갈 수 있는 노드의 숫자만 담기로 했다.
    visit = [False for _ in range(100)] # 방문을 확인하는 노드
    ways = list(map(int, input().split()))
    for i in range(n): # 입력을 노드에 넣는 과정
        node[ways[i*2]].append(ways[i*2 +1])

    def explore(a, g): # a에서 goal을 찾아나가는 여정 / 그래프 경로에서 쓴 함수를 재활용했다.
        for dest in node[a]: # a가 갈 수 있는 길 dest 중
            if not visit[dest]: #  dest를 가본 적이 없을때
                if dest == g: # dest가 g라면 탐색 성공
                    return 1
                # 그렇지 않으면
                visit[dest] = True # 방문 표시를 한 뒤에
                if explore(dest, g): # dest에서 다시 탐색
                    return 1 # 탐색에 실패하면 return하지 않고, 성공일 경우에만 리턴한다.
                visit[dest] = False # 갔다온 뒤에는 다시 방문표시를 지운다.(이 문제에서는 없어도 될 듯 하다.)
        return 0

    visit[0] = True
    return explore(0, 99)



for _ in range(10):
    tc, n = map(int, input().split())
    print('#{} {}'.format(tc, graph(n)))