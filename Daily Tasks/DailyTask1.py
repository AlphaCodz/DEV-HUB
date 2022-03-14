import csv
class Car:
    pay_rate = 0.8 #Pay rate after 20% discount
    all = []
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
        
        #Actions to execute
        
        Car.all.append(self)
        
    def Calculate_Amount(self):
        return ( + self.price * self.quantity)
        
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    def __repr__(self): #To print out the required data in the car instances in readale form
        return f"Car('{self.name}', '{self.type}', '{self.price}')"
    
# for instance in Car.all:
#     print(instance.type)

car1 = Car("Toyota", "SUV", "Cyan", 100, 1)
car1.apply_discount()
print(car1.Calculate_Amount())

# Engine = Car("TYPE2345", "Engine", "Black", 1000, 3)
# Engine.pay_rate = 0.07
# Engine.apply_discount()
# print(Engine.price)

# print(Car.__dict__) #All attribute for class level
# print(Engine.__dict__) #All attribute for instance level

        

