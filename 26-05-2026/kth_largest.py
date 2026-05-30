# Python program to find Kth largest element in list

def logic(arr, k):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr[k-1]

arr = [9, 7, 8, 4, 5, 3]
k = 2
print(logic(arr, k))