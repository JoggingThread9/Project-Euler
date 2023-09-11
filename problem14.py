# longest collatz sequence

# n -> n/2 (n is even)
# n -> 3n + 1 ( n is odd)

largest = 0
current = 0
largest_num = 0

for i in range(1000000, 1, -1):
    num = i
    nums = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            nums += 1
        else:
            num = (3 * num) + 1
            nums += 1

    current = nums

    if largest < nums:
        largest = nums
        largest_num = i

print(largest_num)
