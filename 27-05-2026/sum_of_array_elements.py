# Python program to calculate sum of all array elements recursively.

def sum_of_elements(arr: list):
    if not arr:
        return 0
    return arr[0] + sum_of_elements(arr[1: ])

print(sum_of_elements([10, 0, 10]))
print(sum_of_elements([2, 4, -1, 5, 6]))