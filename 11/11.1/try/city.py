def formatted_city(city, country, population=''):
    '''格式化城市'''
    if population:
        full_city = city + " " + country + " - population " + population
    else:
        full_city = city + " " + country
    return full_city.title()
