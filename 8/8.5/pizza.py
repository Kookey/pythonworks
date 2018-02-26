def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print(toppings)


make_pizza('pepperonis')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza2(*toppings):
    '''概述要制作的比萨'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza2('pepperonis')
make_pizza2('mushrooms', 'green peppers', 'extra cheese')


# 结合使用位置实参和任意数量的实参
def make_pizza3(size, *toppings):
    '''概述要制作的比萨'''
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza3(16, 'pepperoni')
make_pizza3(12, 'mushrooms', 'green peppers', 'extra cheese')