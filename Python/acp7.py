numberlist=[1,2,3,4,5,6]
guessednumber=6 

print("list of numbers are:", numberlist)

h_number=int(input("enter your number:"))

if h_number>guessednumber:
    print ("your number is bigger!")
elif h_number<guessednumber:
    print("your number is too small :(")
else:
    print("Correct! Wohooo")