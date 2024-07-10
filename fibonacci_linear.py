def fibonacci(n):
    a = 0
    b = 1  #initialize to hold the first two values

    if n == 0:
        return 0  #if n is 0 then return zero
    elif n == 1:
        return 1  #same with 1
    else:
        for i in range(2, n+1):  #loop iterates from 2 to n
            c = a + b  #new variable = sum of a and b. represents next # in sequence
            a = b  #value of a is updated to be the previous value of b. shifts a to hold the second-to-last Fib number for the next iteration.
            b = c  #value of b is updated to be the new Fib number c. shifts b to hold the last Fib number for the next iteration.
        return b  #now holds nth number

print(fibonacci(10)) 
        
