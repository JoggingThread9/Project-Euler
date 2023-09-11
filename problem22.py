alphabet = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26}

file = open('p022_names.txt', 'r')
read = file.read()
names = read.split(",")

total = 0
value = 0


for i in range(len(names)):
    value = 0
    for j in names[i]:
        value += alphabet[j]

    value *= i + 1
    total += value

print(total)



