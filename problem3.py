# largest prime factor
num = 600851475143

for i in range(600851475143):
    if num % i == 0:
        if i % 2 != 0:
            if i != num:
                print(i)
                break

