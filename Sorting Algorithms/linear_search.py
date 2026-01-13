def linear_search(arr,target):
    n = len(arr)
    for i in range(len(arr)):
        if arr[i]==target:
            return target,i
    return None 

arr = [1,6,4,0,7]
target = 0
print(linear_search(arr,target))