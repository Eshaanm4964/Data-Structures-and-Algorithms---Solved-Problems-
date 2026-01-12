def find_union(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    freq = {}
    for i in range(len(arr1)):
        freq([arr1][i]) = freq.get(arr1[i],0)+1
    for i in range(len(arr2)):
        freq([arr2][i]) = freq.get(arr2[i],0)+1
    union = sorted(freq.keys())
    return union