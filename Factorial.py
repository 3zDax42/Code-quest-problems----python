testcases = int(input())
for i in range(testcases):
    number = int(input())
    product = 1
    for i in range(1, number+1):
        product *= i
    print(product)
