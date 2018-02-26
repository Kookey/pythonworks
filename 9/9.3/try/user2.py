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


class Privileges():
    """权限"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """管理员"""
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privilege = Privileges()


user = User("Jack", "Li", age=20, address="Sh")
user.describe_user()
user.greet_user()

admin = Admin('Mock', 'Wang', age=30, address='bj')
admin.privilege.show_privileges()
