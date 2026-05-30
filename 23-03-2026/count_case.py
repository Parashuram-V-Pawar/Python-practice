def count_types(s):
    upper = lower = digit = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
    return upper, lower, digit

upper, lower, digit = count_types("Hello123")
print(f"Upper: {upper}")
print(f"Lower: {lower}")
print(f"Digits: {digit}")