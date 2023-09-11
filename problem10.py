# find sum of all primes under 2 million

limit = 2000000

is_prime_array = [True] * limit


def prime_sieve(prime_array):
    for i in range(2, len(prime_array)):
        if prime_array[i]:
            k = i + i
            while k < len(prime_array):
                prime_array[k] = False
                k += i


prime_sieve(is_prime_array)
the_sum = 0

for i in range(2, limit):
    if is_prime_array[i]:
        the_sum += i

print(the_sum)
