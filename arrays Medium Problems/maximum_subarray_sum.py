def maximum_subarray_sum(arr):
    n= len(arr)
    maximum = float("-inf")
    current_sum = 0
    for i in range(len(arr)):
        current_sum+=arr[i]

        if current_sum>maximum:
            maximum = current_sum

        if current_sum<0:
            current_sum = 0

    return maximum
