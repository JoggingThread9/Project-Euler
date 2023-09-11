# number spiral
# start with 1 in the middle and move to the right in a clockwise direction
# 1001 by 1001


def main():
    counter = 0
    gap_size = 1
    four_counter = 4
    total = 0
    for n in range(1, (1001**2 + 1)):
        # count 1, miss one (gap, size), count, miss.... four counter, increase g
        if counter == 0:
            total += n
            counter = gap_size
            four_counter -= 1
            # print('here', n)
        elif counter != 0:
            # print('here2', n)
            counter -= 1
        if four_counter == 0:
            gap_size += 2
            four_counter = 4
    print(total)


main()
