def myPow(x, n):
    if n == 0:
        return 1
    
    if n < 0:
        x = 1 / x
        n = -n
    
    half = myPow(x, n // 2)
    
    if n % 2 == 0:
        return half * half  
    else:
        return x * half * half  

# Example 1
print(myPow(2.00000, 10))  

# Example 2
print(myPow(2.10000, 3))  

# Example 3
print(myPow(2.00000, -2))  
