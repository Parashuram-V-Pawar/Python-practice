# Program to find XOR of all elements in a list
def exor_func(ls: list):
    result = 0
    for i in ls:
        result ^= i
    print(result)

arr = list(map(int, input("Enter array elements: ").split()))
exor_func(arr)