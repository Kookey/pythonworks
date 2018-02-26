def read_file(filename):
    try:
        with open(filename) as animal_obj:
            animal = animal_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        print(animal)


read_file("animal/cats2.txt")
read_file("animal/dogs.txt")
