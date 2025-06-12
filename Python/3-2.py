weight=float(input( "enter your weight in kg :"))
height=float(input("enter your height in cm:"))
BMI= weight/ (height/100)**2

print ("Your BMI is", BMI)
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 34.9:
    print("You are overweight")
elif BMI <= 39.9:
    print("You are severly overweight")
else: 
    print("You are severly obese")

