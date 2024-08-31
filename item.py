class Item:
    def __init__(self, name, bPrice, sPrice):
        self.name = name
        self.bPrice = bPrice
        self.sPrice = sPrice
    
    def display_info(self):
        #Virtual Function to display Item info
        print(f"Name: {self.name}, Buy Price: {self.bPrice}, Sell Price: {self.sPrice}")