import sys

sys.stdin = open('input.txt')

def rec(rst, cnt):
    global n_max
    leng = len(rst)
    if cnt != CHG:
        for i in range(leng-1):
            for j in range(i+1, leng):
                rst[i], rst[j] = rst[j], rst[i]
                rec(rst, cnt +1)
                rst[i], rst[j] = rst[j], rst[i]
    else:
        n_sum = 0
        for i in range(leng):
            n_sum += rst[leng -1 -i] * (10**i)

        if n_sum > n_max:
            n_max = n_sum
    return n_max

# def wiseforce(NUMS, cnt, SRT_NUMS):
#     chg_list = []
#     for i in range(len(NUMS)):
#         if NUMS[i] != SRT_NUMS[i]:
#             chg_list.append(i)
#
#     for c in range(cnt):
#         if len(chg_list) <= c:
#             idx = len(NUMS) - 1
#         else:
#             idx = chg_list[c]
#
#         if idx == len(NUMS) -1:
#             NUMS[idx], NUMS[idx-1] = NUMS[idx-1], NUMS[idx]
#             continue
#
#
#         target = SRT_NUMS[idx]
#         t_idx = 0
#
#         # if target not in NUMS[idx+1:]:
#         #     target = max(NUMS[idx+1:])
#
#         if target < NUMS[idx]:
#             for i in range(len(NUMS)):
#                 if NUMS[i] == target:
#                     t_idx = i
#                     break
#
#         for i in range(len(NUMS)-1, -1, -1):
#             if NUMS[i] == target:
#                 t_idx = i
#                 break
#
#         NUMS[idx], NUMS[t_idx] = NUMS[t_idx], NUMS[idx]
#
#     rtn = 0
#     for i in range(len(NUMS)):
#         rtn += NUMS[len(NUMS) -1 -i] * (10**i)
#
#     return rtn

T = int(input())
for tc in range(1, T+1):
    NUMS, CHG = input().split()
    NUMS = list(map(int, NUMS))
    SRT_NUMS = sorted(NUMS, reverse=True)
    CHG = int(CHG)
    n_max = 0
    print('#{}'.format(tc), wiseforce(NUMS, CHG, SRT_NUMS))
