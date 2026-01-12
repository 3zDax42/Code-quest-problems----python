num = int(input())
for i in range(num):
    FibPos = int(input()) #  0, 1, 1, 2, 3, 5, 8, 13, 21
    temp1 = 0
    temp2= 1
    FibNum = temp1
    for i in range(1, FibPos):
        if i % 2 == 0:
            temp1 += temp2
            FibNum = temp1
        else:
            temp2 += temp1
            FibNum = temp2
    print(f"{FibPos} = {FibNum}")
