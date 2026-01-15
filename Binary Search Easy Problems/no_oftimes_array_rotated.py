def how_many_times_rotated(arr):
    n = len(arr)
    low = 0
    high = n-1
    while low<high:
        mid = (low+high)//2
        if arr[mid]>high:
            low = mid+1
        else:
            high = mid
    return low 
