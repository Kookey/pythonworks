def read_file(filename):
    try:
        with open(filename) as animal_obj:
            animal = animal_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(animal)


read_file("animal/cats2.txt")
read_file("animal/dogs.txt")
