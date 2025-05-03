# print(object, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print("heloo", "world")
print("hello", "word", sep="-")

print("hello", end=" ")
print("world", end=" ")
print("adnan")


# You can write output to a file like this:
with open("output.txt", "w") as c:
    print("Hello File adnan!", file=c)

withfile = open("write.txt", "w")
withfile.write("hello world")


newfile = open("newwirte.txt", "w")
print("Adnan Ahamd", file=newfile)
newfile.close()

# multiple output

name = "adnan"
number = 10.5
age = 20
bool = True 

print(name, number, age, bool)


if age > 18:
    print("you are adult")
else:
    print("you are minor")


for i in range(5):
    print(i)

count = 0 
while count < 5:
    print(count)
    count += 1

send = input("Enter your name: ")

def new(name):
    return f"heloo {name}"

print(new(send))


