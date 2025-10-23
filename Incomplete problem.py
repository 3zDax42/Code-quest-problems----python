Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Repeat = int(input())
for i in range(Repeat):
    InString = input()
    OutString = ""
    for i in InString:
        if i in ['1','2','3','4','5','6','7','8','9','0']:
            OutString += i
        else:
            OutString += " "
    InString = OutString.split()
    OutString = ""
    for i in range(len(InString)):
        OutString += Letters[i-2]
    print(OutString)
