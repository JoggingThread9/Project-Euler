# a**2 + b**2 = c**2
# a + b + c = 1000
a = 1
b = 1

c = (a**2 + b**2) ** .5  # calculates the value of c

for a in range(1,500):  # starts a with a value of 1 in a range of 500
    for b in range(a,500):  # starts b with the value of a with a range of 500
        for c in range(b, 500):  # starts c the value of b with a range of 500
            if a*a + b*b == c*c and a + b + c == 1000:  # checks to see if it is a proper triangle and checks if when values are squared equals 1000
                print(a + b + c)
                print(a * b * c)
