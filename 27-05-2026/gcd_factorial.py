def recursive_gcd(a: int, b: int):
    if b == 0:
        return a
    return recursive_gcd(b, a % b)

print(recursive_gcd(54, 24))
print(recursive_gcd(17, 31))