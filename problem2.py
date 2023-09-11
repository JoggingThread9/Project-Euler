# Fibonacci numbers
num = 2
# starting number
numList = [1, 2]
# first 2 of the Fibonacci numbers

while num < 4000000:
    pos = numList.index(num)
    # finds the position of the num
    num = numList[pos] + numList[pos - 1]
    # takes that num and the num before it and adds them together
    if num > 4000000:
        pass
        # makes sure it does not add a number above 4 mil
    else:
        numList.append(num)
        # adds the new number to numList

num = 0

for i in numList:
    if i % 2 == 0:
        num += i

print(num)
















