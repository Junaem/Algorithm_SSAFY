import  sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    cards = list(input())
    cards_dic = {}

    for card in cards:
        if cards_dic.get(card) != None:
            cards_dic[card] += 1
        else :
            cards_dic[card] = 1

    c_key = ''
    c_max = 1
    for i in range(10):
        if cards_dic.get(str(i)) != None and cards_dic[str(i)] >= c_max:
            c_key = str(i)
            c_max = cards_dic[str(i)]
    print('#{} {} {}'.format(t+1, c_key, c_max))
