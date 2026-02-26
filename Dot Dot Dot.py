import string
def Better_Round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

alphabet = list(string.ascii_lowercase)
n_cases = int(input())
for _ in range(n_cases):
    N_lines = input()
    Dots = 0
    for n in N_lines:
        for i in range(len(alphabet)):
            if n == alphabet[i]:
                Dots += i + 1
    print(Dots)
