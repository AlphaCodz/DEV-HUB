class Sales:
    Shipping_Fee = 50
    in_country_Fee = 20
    def __init__(self, name, category, model, price, quantity, date_of_arrival):
        
        self.name = name
        self.category = category
        self.model = model
        self.price = price
        self.quantity = quantity
        self.date_of_arrival = date_of_arrival
    
    def Shipping(self):
        return self.price * Sales.Shipping_Fee * self.quantity
    
    def In_Country(self):
        return self.price *Sales.in_country_Fee * self.quantity
        
shipping = True       
    
goods1 = Sales('Laptop', 'Computer', 'HP Elitebook220', 150000, 2, '22/4/21')
goods2 = Sales('Makeup Box', 'Fashion', '', 5000, 5, '17/5/20')

if shipping == True:
    print(goods1.Shipping())
else:
    print(goods1.In_Country())
