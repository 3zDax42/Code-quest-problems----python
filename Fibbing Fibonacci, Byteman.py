num = int(input())
for i in range(num):
    FibSearch = int(input()) #  0, 1, 1, 2, 3, 5, 8, 13, 21
    temp1 = 0
    temp2= 1
    FibNum = 0
    i = 1
    Searching = True
    while Searching:
        if FibNum == FibSearch:
            print("TRUE")
            Searching = False
        elif FibNum > FibSearch:
            print("FALSE")
            Searching = False
        if i % 2 == 0:
            temp1 += temp2
            FibNum = temp1
        else:
            temp2 += temp1
            FibNum = temp2
        i += 1
