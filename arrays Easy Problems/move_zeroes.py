def move_zeroes(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i]==0:
            j = i
            break

    for i in range(i+1,len(arr)):
        if arr[i]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
