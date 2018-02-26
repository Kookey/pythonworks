#-*- coding:utf-8 -*-
def city_country(city, country):
    result = city + " " + country
    return result

format_city = city_country('Santiago', 'Chile')
print(format_city)

format_city = city_country('shanghai', 'China')
print(format_city)

format_city = city_country('New York', 'America')
print(format_city)
