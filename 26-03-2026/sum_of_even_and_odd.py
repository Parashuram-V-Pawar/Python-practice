def sum_even_odd(lst):
    even = sum(x for x in lst if x % 2 == 0)
    odd = sum(x for x in lst if x % 2 != 0)
    return even, odd

even_sum, odd_sum = sum_even_odd([1,2,3,4,5])
print(f"Even number sum: {even_sum}\nOdd number sum: {odd_sum}")