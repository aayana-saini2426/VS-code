num = int(input("Enter a number: "))
original_num = num
num_digits = len(str(num))
sum_of_powers = 0
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num = num // 10

if sum_of_powers == original_num:
    print(original_num, "is a Neil Armstrong number.")
else:
    print(original_num, "is not a Neil Armstrong number.")
