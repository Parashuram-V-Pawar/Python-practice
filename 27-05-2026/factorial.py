# Recursive program to calculate factorial of a number

def fact(n: int):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
def main(n):
    if n < 0:
        print("Please enter positive number...")
    else:
        print(fact(n))

main(5)
main(10)