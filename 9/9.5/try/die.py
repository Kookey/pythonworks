from random import randint


class Die():

    """摇骰子"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


die = Die()
die.roll_die()

print("\n")

for x in range(1, 11):
    die.roll_die()

print("10面的色子")
die_10 = Die(sides=10)
for x in range(1, 11):
    die_10.roll_die

print("20面的色子")
die_20 = Die(sides=20)
for x in range(1, 11):
    die_20.roll_die()
