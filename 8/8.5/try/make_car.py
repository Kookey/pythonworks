def make_car(maker, type, **exts):
    '''制作汽车'''
    car = {"maker": maker, "type": type}
    for key, value in exts.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
