import sys

sys.stdin = open('input.txt')

def travel(now, eng, cnt, stops):
    global min_cnt

    if now+eng >= length:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    chg = [0, 0]  # 정류소와 정류소에서 갈 수 있는 곳
    no_chg = [0, 0]
    for move in range(1, eng+1):
        stop = now+move
        chg_eng = stops[stop]
        if stop + chg_eng > chg[1]:
            chg = [stop, stop+chg_eng]

        mo_eng = eng-move
        if stop+mo_eng > no_chg[1]:
            no_chg = [stop, stop+mo_eng]

    chg_st, no_chg_st = chg[0], no_chg[0]
    travel(chg_st, stops[chg_st], cnt+1, stops)
    if chg_st != no_chg_st:
        travel(no_chg_st, eng-(no_chg_st - now), cnt, stops)



T = int(input())
for tc in range(1, T+1):
    stops = list(map(int, input().split()))
    length = len(stops)
    min_cnt = length
    travel(1, stops[1], 0, stops)
    print('#{} {}'.format(tc, min_cnt))
