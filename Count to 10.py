num = int(input())
for i in range(num):
    NumBits = int(input())
    Binary_List = [0 for i in range(NumBits)]

    while True:
        sum = 0
        for i in Binary_List:
            print(i, end= "")
        print()
        for j in Binary_List:
            if j == 1:
                sum +=1
        if sum == NumBits:
            break
        for i in range(NumBits-1, -1, -1): #Last number to fist number in the list
            if Binary_List[i] == 0:
                Binary_List[i] = 1
                break
            else:
                Binary_List[i] = 0
                continue
