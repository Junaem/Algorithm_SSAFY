
nums = [True] * 1000000 # 에라토스테네스의 체
nums[1] = False

for i in range(2, 100000):
    if nums[i]:
        for k in range(i*2, 1000000, i):
            nums[k] = False
for i in range(1, 1000000):
    if nums[i]:
        print(i, end=' ')
