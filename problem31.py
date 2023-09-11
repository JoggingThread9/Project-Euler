# coin sums

# there are eight coins in general circulation
# 1p, 2p, 5p, 10p, 20p, 50p, £1, and £2
# £1 = 100p
# £2 = 200p


# how many ways can £2 be made
ways = 1

for i in range(0, 200 + 1):  # 1
    for j in range(0, 100 + 1):  # 2
        for k in range(0, 40 + 1):  # 5
            for l in range(0, 20 + 1):  # 10
                for m in range(0, 10 + 1):  # 20
                    for n in range(0, 4 + 1):  # 50
                        for o in range(0, 2 + 1):  # 100
                            if i * 1 + j * 2 + k * 5 + l * 10 + m * 20 + n * 50 + o * 100 == 200:
                                ways += 1
                                print(i, j, k, l, m, n, o)

print(ways)
