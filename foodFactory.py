from item import Item

#food class
class Food(Item):
    
    def __init__(self, name, bPrice, sPrice, hp):
        super().__init__(name, bPrice, sPrice)
        self.hp = hp

    def display_info(self):
        print(f"Name: {self.name}, Buy Price: {self.bPrice}, Sell Price: {self.sPrice}, Health Points: {self.hp}")

#The food
corn = Food("Corn", 3, 1, 10)
apple = Food("Apple", 4, 2, 5)
snake = Food("Snake", 5, 3, 15)
chicken = Food("Chicken", 10, 5, 20)

