# 数值相加
while True:
    first_number = input("First number:")
    if first_number == 'q':
        break

    second_number = input("Second number:")
    if second_number == 'q':
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError as e:
        print("string can't case to number")
    else:
        result = first_number + second_number
        print("The result is " + str(result))
