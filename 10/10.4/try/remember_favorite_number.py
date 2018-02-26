import json
number = input("What's your favorite number? ")
number = int(number)
filename = 'favorite_number.json'

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
