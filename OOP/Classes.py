

class Item:
    def Calculate_total_price(self, x, y): 
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.Calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.Calculate_total_price(item2.price, item2.quantity))
# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))