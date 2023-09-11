# smallest multiple

divisors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# makes a list of divisors

for i in range(2520, 999999999999999999, 20):
    # goes through all numbers in that range
    # goes up by 20 because that is the last divisor
    if all(i % j == 0 for j in divisors):
        # checks if all i when divided by all numbers in the divisor list have a remainder of 0
        print(i)
        break
        # stops the program after answer is found
