def majority_element(arr):
    n = len(arr)
    #arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]  
    el = 0
    count = 0
    if count == 0:
        count+=1
        el = arr
    elif el == arr:
        count+=1
    else:
        count-=1
    cnt = arr.count(el)
    if cnt > (n//2):
        return el 
    return -1


