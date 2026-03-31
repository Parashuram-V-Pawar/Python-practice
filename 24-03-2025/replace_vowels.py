def replace_vowels(s):
    vowels = "aeiou"
    return ''.join('*' if ch in vowels else ch for ch in s)

print(replace_vowels("hello"))