# ALGORITHM
#Ask what to order  -- done
#show PRICE of order -- done
# Ask if to proceed with order
#If yes, Order Completed 
#Else, Order Cancelled


class Order:
    shop = 4000
    
    order = input("What do you want to order? ")
    list = ['Plates', 'Phone', 'Accessories', 'Cloths', 'Bags']    
    
    if order in list:
        print("Order Found")
    else:
        print("Order Unavailable for the moment, Please bear with us.")
        quit()
        
    quantity = int(input("Quantity:: "))
        
    def __init__(self, order: str, price: int, quantity: int):
        self.order = order
        self.price = price
        self.quantity = quantity
        
    def total(self):
            order = order1.price * Order.quantity
            return f"Total Price:: N{order}"
            
order1 = Order(Order.order, Order.shop, Order.quantity)            
        
print(order1.total())