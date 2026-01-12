def largest_element_array(arr):
    largest = float("-inf")
    # arr = [2, 5, 1, 3, 0] 
    for i in range(len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

