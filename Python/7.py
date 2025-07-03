lst= ["Divine Rivals", "A good girl's guide to murder", "Powerless", "One of us is lying"]

print("length of the list", len(lst))
print("First element of the list:",lst[0])
print("last element of the list:", lst[-1])
lst.append("shatter me")
print("appended list:", lst)
lst.remove('One of us is lying')
print("updated list:", lst)
lst.sort()
print("sorted list", lst)
lst.reverse()
print("reversed list", lst)
print("list multiplication:", lst*2)

