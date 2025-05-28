name = ['adnan', 'ahamd', 'python', 'prohrammer']
print(name)
print(name[0])
print(name[0:2])


print(name[-1])
print(name[-2])

name[2] = 'python3'

print(name)
new = ['adnan', 'ahamd', 'python', 'prohrammer']
new.append('zain')

print(new)

# insert() — Add item at a specific position

new.insert(1, 'apple')

print(new)

# remove() — Remove an item

new.remove('apple')

print(new)

# pop() — Remove item by index

name.pop(3)

print(name)

# clear() — Empty the list
name.clear()
print(name)

# sort() — Sort the list

number = [1,2, 3, 4, 5, 6, 11, 8, 17, 9, 13, 10]
number.sort()
print(number)

number.reverse()
print(number)


for list in number:
    print(list)

for i in range(len(number)):
    print(number[i])



list_variable = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_variable[0] = 10

print(f'this vbara frist list {list_variable}')

list_variable[0:3] = [100, 200, 300]

print(list_variable)


if 9 in list_variable:
    print('yes')


# 📚 Python Data Types: List vs Tuple vs Set vs Dictionary

# Feature	List	Tuple	Set	Dictionary
# Ordered	✅ Yes	✅ Yes	❌ No	✅ Yes
# Changeable	✅ Mutable	❌ Immutable	✅ Mutable	✅ Mutable
# Duplicates	✅ Allowed	❌ Allowed	❌ Not allowed	❌ Keys not allowed
# Indexed	✅ Yes	✅ Yes	❌ No	✅ Key-based (not index)
# Syntax	[ ] brackets	( ) parentheses	{ } curly braces	{key: value} curly braces