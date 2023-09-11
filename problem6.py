# sum of squares
num1 = 0
for i in range(1, 101):
    num1 += i**2
    # for evert number in 1-100 squares it then adds it to num1

# square sum
num2 = 0
for i in range(1, 101):
    num2 += i
    # for every number in 1-100 adds it to num2
num2 = num2**2
# squares num2

# sum square difference
ans = num2 - num1
# subtracts num1 from num2 to find the difference
print(ans)
# prints the answer
