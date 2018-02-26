with open("learning_python.txt") as learning_object:
    contents = learning_object.read()
    print(contents)

print("\n")
with open("learning_python.txt") as learning_object:
    for line in learning_object:
        print(line.rstrip())

print("\n")

with open("learning_python.txt") as learning_object:
    lines = learning_object.readlines()

for line in lines:
    print(line.strip())
