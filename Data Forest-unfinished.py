def SplitList(NumList, CallNum = 0):
    Mid = NumList[len(NumList)//2]
    List1 = []
    List2 = []
    print("   " * (len(NumList)//2), end="")
    if CallNum == 0:
        print(Mid)
    else: print(Mid, end="")
    for i in NumList:
        if i < Mid:
            List1.append(i)
        elif i > Mid:
            List2.append(i)
    CallNum+= 1
    if len(List1) == 1:
        print(List1[0], end="   ")
        print(List2[0])
        return
    else:
        SplitList(List1, CallNum)
        SplitList(List2, CallNum)

testcases = int(input())
for i in range(testcases):
    imput = input().split()
    numbers = []
    for i in imput:
        numbers.append(int(i))
    numbers.sort()
    print(numbers)
    SplitList(numbers)
