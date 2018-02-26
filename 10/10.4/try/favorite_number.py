import json

filename = 'favorite_number.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
except FileNotFoundError as e:
    number = input("What's your favorite number? ")
    number = int(number)
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
else:
    print("I know your favorite number! It's " + str(number))
