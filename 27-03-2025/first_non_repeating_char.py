def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

print(first_non_repeating("aabbcde"))