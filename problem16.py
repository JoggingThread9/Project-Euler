# power digit sum

num = 2 ** 1000
# calculates 2 to the 1000
num = str(num)
# makes num into a string so it can be accessed
numList = []

for i in num:
    numList.append(i)
    # adds each number of num into numList as a element of the list

ans = int(numList[0])
# makes a variable with the first number of numList as a integer

for i in numList[1:]:
    ans += int(i)
    # goes through numList and adds it to start number each time

print(num)
print(numList)
print(ans)
# prints all the variables
