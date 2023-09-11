# 10001st prime number

prime_numbers = []
j = 2


def prime(n, prime_numbers):
    # loops through prime_numbers and checks
    for i in range(2, len(prime_numbers) - 1):
        # checks if it is prime
        if n % i == 0:
            # if it is not prime
            return False


# finds the 10001 prime number
while len(prime_numbers) < 10002:
    # calls the prime function using the inputted values
    value = prime(j, prime_numbers)
    # if it is a prime
    if not value:
        prime_numbers.append(j)
    # increases j
    j += 1

print(max(prime_numbers))
