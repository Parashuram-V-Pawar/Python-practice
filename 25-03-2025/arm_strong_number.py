def armstrong(n):
    temp = n
    digits = len(str(n))
    sum_val = 0
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** digits
        temp //= 10
    return sum_val

n = 153
if (armstrong(n) == n):
    print("Arm strong number")
else:
    print("Not a armstrong number")