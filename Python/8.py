my_tuple=()
print(my_tuple)

#to print integers

my_tuple=(0,1,2,3)
print(my_tuple)

#to print string & decimals
my_tuple=(0,1,2,3,4.5, "hello")
print(my_tuple)

#nested 
my_tuple=("hello", [0,1,2], [ 3,4,5])
print(my_tuple)

my_tuple= ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[4])

#nested 
n_tuple=('mouse', [1,2,3], (4,5,6))
print(n_tuple[0][3])
print(n_tuple[1][2])

print("slice:", my_tuple[1:4])

for letter in (my_tuple):
    print("hello", letter)