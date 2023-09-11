cap = 1000000
power = 5

nums = []

for number in range(2, cap+1):
    total = 0
    for digit in str(number):
        total += int(digit) ** power

    if total == number:
        nums.append(number)

print(sum(nums))
