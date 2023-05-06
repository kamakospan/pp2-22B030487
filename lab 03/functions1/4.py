def filter_prime(nums):
    primenumbers = []
    isPrime = True

    for number in nums:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                isPrime = False
                break
        if isPrime is True:
            primenumbers.append(num)
        isPrime = True
    return primenumbers
nums = list(map(int, input().split()))
print(filter_prime(nums))