

class Food:
    
    def __init__(self, name, bPrice, sPrice, hp):
        self.name = name
        self.bPrice = bPrice
        self.sPrice = sPrice 
        self.hp = hp

    def get_name(self):
        return self.__name 
    
    def set_name(self, name):
        self.__name = name

    def display_info(self):
        print(f"Name: {self.name}, Buy Price: {self.bPrice}, Sell Price: {self.sPrice}, Health Points: {self.hp}")

#The food
corn = Food("Corn", 3, 1, 10)
apple = Food("Apple", 4, 2, 5)
snake = Food("Snake", 5, 3, 15)
chicken = Food("Chicken", 10, 5, 20)

