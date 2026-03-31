
def factorial(n, fact):
    for i in range(1, n+1):
        fact *= i
    return fact

n = 5
fact = 1
print(factorial(n,fact))