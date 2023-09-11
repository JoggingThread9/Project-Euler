# distinct powers

min = 2
max = 100

nums = []

for a in range(min, max+1):
    for b in range(min, max+1):
        num = a**b
        if num not in nums:
            nums.append(num)
        else:
            pass

nums.sort()
print(len(nums))
