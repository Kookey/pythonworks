# 数值相加

first_number = input("First number:")
second_number = input("Second number:")
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError as e:
    print("string can't case to number")
else:
    result = first_number + second_number
    print("The result is " + str(result))
