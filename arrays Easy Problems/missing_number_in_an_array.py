def missing_number(arr,n):
    #[1,2,4,5] miss_no = 3 n = 
    N = (n*(n+1))//2
    actual_sum = sum(arr)
    return N -actual_sum

