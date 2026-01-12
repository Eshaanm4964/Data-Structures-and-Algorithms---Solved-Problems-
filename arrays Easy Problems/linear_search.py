def linear_search(arr,target):
    if len(arr)==0:
        return None
    #arr = [1,2,3,4,6,8] target = 4
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return False

