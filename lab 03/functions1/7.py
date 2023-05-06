def barma33(nums):
    isTrue = False
    for i in range(1, len(nums)):
        num = nums[i] * 10 + nums[i-1]
        if num == 33:
            isTrue = True
            break
    return isTrue
nums = list(map(int, input().split()))
print(barma33(nums))