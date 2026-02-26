def Better_Round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

n_cases = int(input())
for _ in range(n_cases):
    N_lines = input().split('"')
    for i in N_lines:
        if i in [" ", ""]:
            N_lines.remove(i)
    Sentence1 = N_lines[1].split()
    Sentence2 = N_lines[2].split()
    Words = N_lines[0]
    Words = "".join([c for c in Words if c not in [" ", "[", "]"]])
    Words = Words.split(',')
    Letters = []
    for i in Sentence1[int(Words[0]) - 1]:
        Letters.append(i)
    
    if len(Letters) == len(Sentence2[int(Words[1]) - 1]):
        for i in range(len(Letters)):
            if Sentence2[int(Words[1]) - 1][i] in Letters:
                Letters.remove(Sentence2[int(Words[1]) - 1][i])
            else:
                print("Intercepted")
                break
        else:    
            print("Verified")
    else:
        print("Intercepted")
