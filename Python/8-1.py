myset={1,1,2,2,2,3,3,4,}
print(myset)

myset.add(5)
print('updated set',myset)

set1=myset
set2={2,9,8,7}

print('difference')
print(set1.difference(set2))
print('symmetric difference')
print(set1.symmetric_difference(set2))
