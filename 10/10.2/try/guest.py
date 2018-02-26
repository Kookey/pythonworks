# 记录访客名单并写入文件中
while True:
    name = input("What's your name? ")
    if name == 'q':
        break
    with open("guest.txt", 'a') as file_object:
        file_object.write(name + "\n")
