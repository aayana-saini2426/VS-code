def intro(name): 
    print("hello,good morning i am", name)
user_name=input("Enter your name:")
intro(user_name)

def grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "F"
marks=int(input("Enter your marks:"))
grade=grade(marks)
print("YOUR GRADE IS", grade)