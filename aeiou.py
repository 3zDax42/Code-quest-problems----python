num = int(input())
for t in range(num):
    variable = input()
    vowels = 0
    for i in variable:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    print(vowels)
