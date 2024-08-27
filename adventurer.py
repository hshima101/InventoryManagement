from foodFactory import Food

class Adventurer:

    def __init__(self, name):
        self.name = name
        self.__inventory = []

    def add_food(self, food):
        if isinstance(food, Food):
            self.__inventory.append(food)
        else:
            print(f"Cannot add {food}. It is not a Food object")

    def display_inventory(self):
        print(f"\n{self.name}'s Inventory: ")
        for food in self.__inventory:
            food.display_info()

tim = Adventurer("Tim")