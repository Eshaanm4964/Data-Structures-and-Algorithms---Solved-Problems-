def rotated_array(arr,x):
    n = len(arr)
    low = 0
    high = n-1 
    # arr = [4,5,6,0,1,2] k = 0
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid 
        
        if arr[low]<=arr[mid]:
            if arr[low]<=x<arr[mid]:
                high = mid-1
            else:
                low = mid+1
        
        else:
            if arr[mid]<x<=arr[high]:
                low = mid+1
            else:
                high = mid-1 
    
    return -1 
