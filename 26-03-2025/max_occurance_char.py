def max_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get)

print(max_char("banana"))