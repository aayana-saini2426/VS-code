def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result
students=[['1', "myra", "air"], ['2', 'ravi', 'fire'] , ['3', 'riya', 'earth']]
print("\nOriginal list of lists:")
print(students)
print('\nConverted lists to dictionary')
print(test(students))