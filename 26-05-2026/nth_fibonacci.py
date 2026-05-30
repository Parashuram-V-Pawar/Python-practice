# Program to find nth fibonacci number

def fibonacci(n: int):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def nth_fib(n):
    arr = []
    if n <= 0:
        print("Enter a positive integer...")
    else:
        for i in range(n):
            arr.append(fibonacci(i))
        print(arr[n-1])

nth_fib(6)
nth_fib(2)
nth_fib(1)
nth_fib(10)