testcases = int(input())
for i in range(testcases):
    numbers = input().split()
    if numbers[1] == "+":
        result1 = int(numbers[0]) + int(numbers[2])
        result2 = int(numbers[2]) + int(numbers[0])
    elif numbers[1] == "-":
        result1 = int(numbers[0]) - int(numbers[2])
        result2 = int(numbers[2]) - int(numbers[0])
    elif numbers[1] == "/":
        result1 = int(numbers[0]) / int(numbers[2])
        result2 = int(numbers[2]) / int(numbers[0])
    elif numbers[1] == "*":
        result1 = int(numbers[0]) * int(numbers[2])
        result2 = int(numbers[2]) * int(numbers[0])
    result1 = round(result1+.0001, 1) / 1
    result2 = round(result2+.0001, 1) / 1
    print(result1, result2)
