class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("restaurant's name is " + self.restaurant_name.title() + " and restaurant's type " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is now open.")

my_restaurant = Restaurant('KFC', 'snack')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
