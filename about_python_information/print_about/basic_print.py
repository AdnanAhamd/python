# basic print value
print("hello world")

print('''     

      *** Adnan Ahmad ***
      *** Python programmer ***


 ''')

# f string

name = "Adnan Ahamd"
language = "pythan"

print(f"hello {name} is {language} programmer")


# age

age = 20 

add = f"My age is {age+3}"

print(add)

# using in if statment

age = 5

if age > 18:
   print("you are adult")
else:
   print("yor are minor")

# using in for loop

for i in range(5):
   print(i)

# using in while loop

count = 0 

while count < 5:
   print(count)
   count += 1

# using in function string

def greet(name):
   return f"hello {name}"
print(greet("Adnan"))
