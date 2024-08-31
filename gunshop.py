from item import Item

#our adventurer needs weapons to choose from
#maybe weapons should be its own class of items

#weapon class
class Weapon(Item):
    def __init__(self, name, bPrice, sPrice, atk, mag, bullet):
        super().__init__(name, bPrice, sPrice)
        self.atk = atk
        self.mag = mag
        self.bullet = bullet

    def display_info(self):
        print(f"Name: {self.name}, Buy Price: {self.bPrice}, Sell Price: 
              {self.sPrice}, Attack Points: {self.atk}, Magazine Size: {self.mag}, 
              Bullet Type: {self.bullet}")
        
#the weapons
AR15 = Weapon("AR-15", 500, 250, 25, 30, .223)
AK47 = Weapon("AK-47", 400, 200, 50, 30, 7.62)