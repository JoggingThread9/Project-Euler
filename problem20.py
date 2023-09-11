# factorial
from math import factorial


def fact(num):
    product = num
    for i in range(num - 1, 1, -1):
        product *= i

    product = str(product)
    sum = 0

    for i in range(len(product)):
        sum += int(product[i])

    return sum


print(fact(100))

