
# class item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def Calculate_Purchase(self):
#         return self.price * self.quantity
        

# item1 = item("Food", 2500, 3)

# print(item1.cap)
# print(item1.Calculate_Purchase())
    
# print(item1.name)
      
      
    #   CHECK IF I UNDERSTAND BY BUILDING A CAR CLASS
    
class Car:
    def __init__(self, name: str, type: str, color: str, price: float, quantity = 0):
        #Run Validation to received Arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity>= 0, f"Quantity {quantity} is not greater than or equal to Zero"
        
        # Assign to Self Object
        self.name = name
        self.type = type
        self.color = color
        self.price = price
        self.quantity = quantity
        
        
    def Calculate_Amount(self):
        return self.price * self.quantity
        
    
car1 = Car("Toyota", "SUV", "Cyan", 350000, 4)
print(car1.Calculate_Amount())
        

