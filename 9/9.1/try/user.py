class User():
    """用户简介"""
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print("Full name: " + self.first_name + " " + self.last_name)
        for key, value in self.user_info.items():
            print(key + ": " + str(value))

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name + "!")


user = User("Jack", "Li", age=20, address="Sh")
user.describe_user()
user.greet_user()
