number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(number)
print(number[0])
print(number[0][1])
print(number[0][1:3])

# Assign list elements into variables directly:
person = ['alice', 1, 'new york']


age, name, city = person
print(age, name, city)

#  With * operator (grab multiple items):

a, *b = [1, 2, 3, 4, 5]
print(a, b)