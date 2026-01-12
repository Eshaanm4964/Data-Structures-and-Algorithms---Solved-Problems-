def remove_duplicates(arr):
    index = 0
    seen = set()
    for num in arr:
        if num not in arr:
            seen.add(num)
            index[num] = num
            index+=1
    return index