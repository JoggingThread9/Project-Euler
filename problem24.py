# lexicographic permutations
# find the 1 millionth lexicographical permutation

import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test = [0, 1, 2, 3]


def permute(digits):
    permutations = []

    perm = itertools.permutations(digits)

    for i in list(perm):
        permutations.append(i)

    return permutations[999999]


print(permute(digits))
