filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming111.\r\n")
    # 写入多行
    file_object.write("I love creating new games.\r\n")


# 追加模式
with open(filename, 'a') as file_object:
    file_object.write("I love programming111.\r\n")
    # 写入多行
    file_object.write("I love creating new games.\r\n")
