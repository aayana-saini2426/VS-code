def factorial(n):
    if n==1: 
        return 1
    else:
        return n*factorial(n-1)
    
number=int(input("enter no."))
result= factorial(number)
print(result)