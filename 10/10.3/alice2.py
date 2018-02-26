fileanme = 'alice.txt'
try:
    with open("fileanme") as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    print("Sorry, the file " + fileanme + " does not exist")
