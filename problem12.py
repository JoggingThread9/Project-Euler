# triangle numbers
# ex) 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
# over five hundred divisors

from math import floor, sqrt

divisor = 0


def triangle(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def divisors(n):
    divs = 0
    for i in range(1, floor(sqrt(n))+ 1):
        if n % i == 0:
            if i ** 2 != n:
                divs += 2
            else:
                divs += 1
    return divs


i = 1

while divisors(triangle(i)) <= 500:
    i += 1

print(triangle(i))



