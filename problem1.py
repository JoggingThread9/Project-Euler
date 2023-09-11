total = 0
numList = []
for i in range(1000):
    if i % 3 == 0:
        if i in numList:
            pass
        else:
            numList.append(i)

    if i % 5 == 0:
        if i in numList:
            pass
        else:
            numList.append(i)

num = numList[0]
for i in numList[1:]:
    num += i

print(num)
