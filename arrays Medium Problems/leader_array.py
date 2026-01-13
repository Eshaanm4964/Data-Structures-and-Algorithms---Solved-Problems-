def leaders(arr):
    n = len(arr)
    leaders = []
    lead = arr[-1]
    leaders.append(arr[-1])
    for i in range(n-2,-1,-1):
        if lead<arr[i]:
            leaders.append(arr[i])
            lead = arr[i]
    leaders.reverse()
    return leaders 

arr = [10, 22, 12, 3, 0, 6]  
print(leaders(arr))