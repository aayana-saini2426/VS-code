
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num_terms = int(input("Enter how many Fibonacci numbers to print: "))

print("Fibonacci sequence:")

for i in range(num_terms):
    print(fibonacci(i))
