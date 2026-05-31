# Program to reverse a string recursively.

def reverse_string(s: str):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))
print(reverse_string("madam"))