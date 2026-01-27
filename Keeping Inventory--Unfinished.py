
def BubbleSort(OrignList):
    NumList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "O"]
    for l in range(len(OrignList)-1):
        for j in range(len(OrignList)-l-1):
            for i in range(len(OrignList[j])):
                try:
                    if (OrignList[j][i] == "/") and (OrignList[j+1][i] != "/"):
                        temp = OrignList[j]
                        OrignList[j] = OrignList[j+1]
                        OrignList[j+1] = temp
                    elif (OrignList[j][i] == ".") and (OrignList[j+1][i] != "."):
                        temp = OrignList[j]
                        OrignList[j] = OrignList[j+1]
                        OrignList[j+1] = temp
                    elif (OrignList[j][i] == "-") and (OrignList[j+1][i] != "/"):
                        temp = OrignList[j]
                        OrignList[j] = OrignList[j+1]
                        OrignList[j+1] = temp
                    elif (OrignList[j][i] in NumList) and (OrignList[j+1][i] not in NumList):
                        temp = OrignList[j]
                        OrignList[j] = OrignList[j-1]
                        OrignList[j-1] = temp
                    elif (OrignList[j][i] > OrignList[j+1][i]):
                        temp = OrignList[j]
                        OrignList[j] = OrignList[j+1]
                        OrignList[j+1] = temp
                    else:
                        continue
                except:
                    break
    return OrignList


TestCases = int(input())

UnsortedList = []
for i in range(TestCases):
    UnsortedList.append(input())

SortedList = BubbleSort(UnsortedList)
print(SortedList)
