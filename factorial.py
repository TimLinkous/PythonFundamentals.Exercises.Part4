def factorial(n):
    while (n >= 0 and n < 995):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
print(factorial(6))