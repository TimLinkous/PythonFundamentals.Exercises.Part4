
#x(n - 1) + x(n - 2)

def fibonacci(n):
    while n >= 0 and n <= 30:
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(12))