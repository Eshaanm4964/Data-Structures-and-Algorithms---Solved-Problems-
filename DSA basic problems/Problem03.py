def palindrome(n):
    reverse_number = 0 
    dup = n 
    while n > 0:
        ld = n % 10 
        reverse_number = (reverse_number * 10) + ld  
        n //= 10  
    return dup == reverse_number