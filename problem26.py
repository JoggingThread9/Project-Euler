# reciprocal cycles
# uses long division

def main():
    d = 1000
    greatest_cycle_length = 0
    greatest_d = None
    for i in range(1,d):

        current = find_cycle_length(i)

        if greatest_cycle_length < current:
            greatest_cycle_length = current
            greatest_d = i

    print(greatest_d)


def find_cycle_length(n):
    cycle_length = 1
    list_of_remainders = []
    x = 1

    while True:
        if x % n == 0:
            break
        elif x in list_of_remainders:
            break
        list_of_remainders.append(x)
        x = (x*10) % n
        cycle_length +=1

    return cycle_length


main()