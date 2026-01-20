TestCases = int(input())
for i in range(TestCases):
    NumberList = []
    NumberList.append(input().split())
    NumberList[0][0] = int(NumberList[0][0])
    NumberList[0][1] = int(NumberList[0][1])
    while int(NumberList[-1][0]) > 1:
        NumberList.append(
            [int(NumberList[-1][0])/2,
            int(NumberList[-1][1])*2])
    DoublesSum = 0
    for i in NumberList:
        if i[0]%int(i[0]) > 0:
            print(int(i[0])//1, "*", end=" ", sep="")
        else:
            print(int(i[0])//1, end=" ")
        if int(i[0])%2 == 1:
            print(i[1])
            DoublesSum += int(i[1])
        else:
            print(i[1], "***")
    print(DoublesSum)
