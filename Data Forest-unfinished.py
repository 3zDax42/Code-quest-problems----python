def SplitList(NumList, CallNum = 0):
    Mid = NumList[len(NumList)//2]
    List1 = []
    List2 = []

    for i in NumList:
        if i < Mid:
            List1.append(i)
        elif i > Mid:
            List2.append(i)

    #print(Mid)

    

    print("   " * (len(NumList)//2), end="")
    if len(str(Mid)) == 1:
        print("  ", end="")
    elif len(str(Mid)) == 2:
        print(" ", end="")
    if CallNum == 0:
        print(Mid)
    else:
        print(Mid, end="")
    
    if len(List1) != 1:
        a, b = SplitList(List1, CallNum+1)
        c, d = SplitList(List2)
    else:
        # print(List1[0], end="   ")
        # print(List2[0])
        return List1[0], List2[0]
    print(a, "   ", b, "   ", c, "   ", d)

testcases = int(input())
for i in range(testcases):
    imput = input().split()
    numbers = []
    for i in imput:
        numbers.append(int(i))
    numbers.sort()
    print(numbers, "Not in function")
    SplitList(numbers)
