num = int(input())
for t in range(num):
    Number_List = input().split()
    Highest_Number = 0
    for u in range(len(Number_List)):
        if int(Number_List[u]) > Highest_Number:
            Highest_Number = int(Number_List[u])
    print(Highest_Number)
