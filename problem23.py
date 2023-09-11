# non abundant sums

# find abundant numbers
# every abundant number to a different one to fin all the numbers that are sums of abundant number
# add all those number together


def factorise(x):
    d = 1
    divisors = []
    while d < x:
        if x % d == 0:
            divisors.append(d)
        d += 1
    total_of_divisors = sum(divisors)
    return total_of_divisors


def main():
    number_to_sum_to = 28123
    test_number = 1
    dict_of_numbers = {}

    for i in range(number_to_sum_to):
        dict_of_numbers[i] = i
    list_of_abundant_numbers = []

    for i in range(number_to_sum_to):
        x = factorise(i)
        if x > i:
            list_of_abundant_numbers.append(i)

    for j in range(len(list_of_abundant_numbers)):
        for i in range(len(list_of_abundant_numbers)):
            if list_of_abundant_numbers[j] + list_of_abundant_numbers[i] in dict_of_numbers:
                dict_of_numbers.pop(list_of_abundant_numbers[i] + list_of_abundant_numbers[j])

    total = sum(dict_of_numbers.values())
    print(total)


main()