def lower_bound(arr,n,x):
    low = 0
    high = n-1
    ans = n
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def row_max_ones(matrix,n,m):
    cnt_max = 0
    index = -1
    for i in range(n):
        cnt_ones = m - self.lower_bound(matrix[i],m,1)
        if cnt_ones >cnt_max:
            cnt_max = cnt_ones
            index = i
    return index