def binary_search(arr,x):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
         
        if arr[mid] ==x:
            return mid
        
        elif arr[mid] > x:
            high = mid-1 
        
        else:
            high = mid+1

    return -1 