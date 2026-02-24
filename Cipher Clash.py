def Better_Round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.0002))
    return result / 10**n_digits
n_cases = int(input())

for _ in range(n_cases):
    N_Input = input().split('"')
    for i in N_Input:
        if i == '' or i == ' ':
            N_Input.remove(i)
    Word = N_Input[0]
    N_Input.remove(Word)
    Word = "".join([c for c in Word if c not in ["[", "]"]]) #removing characters from a string
    Word = Word.split(',')
    Sentence1 = N_Input[0].split()
    Sentence2 = N_Input[1].split()
    Letters = []
    for i in Sentence1[int(Word[0])]:
        Letters.append(i)
    
    print(Word)
    print(Sentence1)
    print(Sentence2)
