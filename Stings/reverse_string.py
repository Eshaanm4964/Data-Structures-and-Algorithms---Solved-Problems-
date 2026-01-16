def reverse_string(str):
    result = []
    for ch in range(len(str)-1,-1,-1):
            result.append(str[ch])
    return "".join(result) 

str = "Eshaan"
print(reverse_string(str))
