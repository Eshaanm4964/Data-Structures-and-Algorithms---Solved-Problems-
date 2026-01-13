def rearrage_positive_negative(arr):
    n = len(arr)
    array = [0]*n
    pos = 0
    neg = 1
    for i in range(len(arr)):
        if arr[i]<0:
            array[neg] = arr[i]
            neg+=2
        else:
            array[pos] = arr[i]
            pos+=2
    return array

arr = [1,2,-4,-5]
print(rearrage_positive_negative(arr))

