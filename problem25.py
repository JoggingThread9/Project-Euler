# 1000 digit fibonacci number

# recurrence relation -> F_n = F_n-1 + F_n-2 where F_1 = 1 and F_2 = 1

def fibonacci():
    F = [1, 1]

    pos = 1
    while True:

        F.append(F[pos] + F[pos-1])

        pos += 1

        num = F[pos]

        if len((str(num))) == 1000:
            break

    return F.index(num) + 1


print(fibonacci())

