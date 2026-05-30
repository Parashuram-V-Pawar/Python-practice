def second_smallest(lst):
    first = second = float('inf')

    for num in lst:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num

    return second

print(second_smallest([4,2,1,3]))