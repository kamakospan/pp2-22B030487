import math

max_num = int(input())

nums = range(2, max_num)

for i in range(2, max_num):
    nums = filter(lambda x: x == i or x % i, nums)
print(list(nums))