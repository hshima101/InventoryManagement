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

    #sorting functions
    def sort_inventory_alpha(self):
        self.__inventory.sort(key=lambda food: food.name)
        print(f"\n{self.name}'s Sorted Inventory (Alphabetically):")
        for food in self.__inventory:
            food.display_info()

    def sort_inventory_hp(self):
        self.__inventory.sort(key=lambda food: food.hp, reverse=True)
        print(f"\n{self.name}'s Sorted Inventory (by HP, Largest to Smallest): ")
        for food in self.__inventory:
            food.display_info()

    #total sum functions
    def buy_price_sum(self):
        total_buy_price = sum(food.bPrice for food in self.__inventory)
        print(f"\nTotal Buy Price of Inventory: {total_buy_price}")
        return total_buy_price

    def sell_price_sum(self):
        total_sell_price = sum(food.sPrice for food in self.__inventory)
        print(f"\nTotal Buy Price of Inventory: {total_sell_price}")
        return total_sell_price
    
    def hp_sum(self):
        total_hp = sum(food.hp for food in self.__inventory)
        print(f"\nTotal Buy Price of Inventory: {total_hp}")
        return total_hp 
    
tim = Adventurer("Tim")