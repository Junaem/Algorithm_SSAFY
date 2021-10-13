import sys

sys.stdin = open('input.txt')

def baby(cards):
    hands= [[], [0 for _ in range(10)], [0 for _ in range(10)]]

    for i in range(12): # 플레이어에 카드 넣기
        player = 1
        card = cards[i]
        if i%2:
            player = 2
        hands[player][card] +=1

        start = card-2
        if start < 0:
            start = 0

        for c in range(start, card+1): # 카드 검사
            n_card = hands[player][c]
            if n_card:
                if n_card == 3:
                    return player
                if c < 8 and hands[player][c+1] and hands[player][c+2]:
                    return player

    return 0




T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, baby(cards)))