absent=int(input("Enter the no. of days you were absent:"))
total_days=30 

print("The days you were absent are:", absent)
print("Total days were", total_days)

percentage= (total_days-absent)/total_days * 100 

if percentage>=75:
    print("You can give the examination", percentage)
else:
    print("You cannot give the examination as you percentage is", percentage)