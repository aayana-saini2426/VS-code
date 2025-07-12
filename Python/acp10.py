class Expression:
        def __init__(self, num1, num2, num3):
            self.num1 = num1
            self.num2 = num2
            self.num3 = num3
        def calculate_sum(self):
            total_sum = self.num1 + self.num2 + self.num3
            print(f"The sum of the three numbers is: {total_sum}")
expression1 = Expression(10, 20, 30)
expression2 = Expression(5, 15, 25)


expression1.calculate_sum()
expression2.calculate_sum()