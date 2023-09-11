# amicable numbers

amicable_nums = []


def d(num):
    for i in range(1, num):
        divisor_num = []
        for j in range(1, i):
            if i % j == 0:
                divisor_num.append(j)

        total = sum(divisor_num)

        divisor_total = []

        determiner = False

        if i == total:
            determiner = True

        if determiner:
            pass
        else:
            for k in range(1, total):
                if total % k == 0:
                    divisor_total.append(k)

            if i == sum(divisor_total):
                amicable_nums.append(i)

    return amicable_nums


print(d(10000))
print(sum(amicable_nums))
