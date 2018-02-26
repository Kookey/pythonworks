with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)
    # 去掉空行
    print(contents.rstrip()
