def barma007(nums):
    is007 = False
    for i in range(2, len(nums)):
        agent = nums[i-2] * 100 + nums[i-1] * 10 + nums[i]
        if agent == 7:
            is007 = True
            break
    return is007
nums = list(map(int, input().split()))
print(barma007(nums))