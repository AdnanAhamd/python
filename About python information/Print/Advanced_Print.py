# print(object, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print("heloo", "world")
print("hello", "word", sep="-")

print("hello", end=" ")
print("world", end=" ")
print("adnan")


# You can write output to a file like this:
with open("output.txt", "w") as f:
    print("Hello File!", file=f)

