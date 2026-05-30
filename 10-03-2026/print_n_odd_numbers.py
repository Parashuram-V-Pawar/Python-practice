def print_n_odd_numbers(n):
    count = 0
    for i in range(n):
        print(2*i +1)

n = int(input("Enter a number: "))
print_n_odd_numbers(n)