# quadratic primes

# find the products of the coefficients a and b
# where |a| < 1000 and |b| <= 1000 and n = |n|
# formula = n**2 + (a*n) + b


# n**2 + n + 41 will return 40 primes for 0<= n <= 39

# n**2 - 79n + 1061 will return 80 primes for 0 <= n <= 79


def is_prime(num):
    prime = True
    if num % 2 == 0:
        return False

    for i in range(3, abs(num), 2):
        if abs(num) % i == 0:
            prime = False
            break

    return prime


largest_n_primes = 0
largest = 0
n_of_primes = 0

for a in range(-999, 1000):
    print(a)
    for b in range(-1000, 1000 + 1):
        n = 0
        n_of_primes = 0
        while True:
            if is_prime(n**2 + (a*n) + b):
                n_of_primes += 1
            else:
                if n_of_primes > largest_n_primes:
                    largest_n_primes = n_of_primes
                    largest = a*b
                break
            n += 1

print(largest)