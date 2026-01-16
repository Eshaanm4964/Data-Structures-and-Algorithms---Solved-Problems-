def string_palindrome(str):
    n = len(str)
    l = 0
    r = n-1
    while l<r:
        if str[l]!=str[r]:
            return False
        l+=1
        r-=1
    return True 
