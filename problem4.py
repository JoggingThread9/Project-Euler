products = []

for num1 in range(100, 999):
    # loops through all three-digit numbers
    for num2 in range(100, 999):
        # loops through all three-digit numbers
        product = num1 * num2
        # multiplies these numbers
        if product in products:
            # checks to see if that product has already been found
            pass
        else:
            if str(product) == str(product)[::-1]:
                products.append(product)
                # if the product equals the product backwards then adds it to a list

compare = products[0]
# gives a initial value to compare with
for i in products:
    # loops through all elements inside of products
    if i > compare:
        compare = i
        # if i is greater than the compare value compare noe equals i


print(compare)
# prints the largest palindrome number
