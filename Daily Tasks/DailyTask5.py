# Banking System: That Allows creation of account, depositing and withdrawal of funds
name = input("What is your name? ")

gender = input("Gender(M/F): ")

if gender == "m".upper():
    print("Welcome to Assurance Bank, Mr " + name)

else:
    print("Welcome to Assurance Bank, Mrs " + name)


age = int(input("How old are you? "))

LGA = input("LGA: ")

State_of_origin = input("State_of_Origin: ")

State_of_Residence = input("State of Residence: ")

address = input("Address: ")

Nationality = input("Nationality: ")

print(" Account Successfully Created!\
    Thank You for choosing Assurance Bank! ")



class Bank:
    fund = float(input("Deposit_Amount:: "))
    Initial_Account_Balance = 0.00
    withdraw = float(input("Withdrawal_amount:: "))
    
    def __init__(self, name: str, age: int, LGA: str, State_of_origin: str, State_of_Residence: str, Address, Nationality: str, deposit: float, \
        withdraw: str):
        self.name = name
        self.age = age
        self.local_govt = LGA
        self.State_of_origin = State_of_origin
        self.State_of_residence = State_of_Residence
        self.address = Address
        self.Nationality = Nationality
        self.deposit = deposit
        self.withdraw = withdraw
        
         
    def Deposit(self):
        
        Bank.Initial_Account_Balance = Bank.Initial_Account_Balance + Bank.fund
        
        return f"Balance: {Bank.Initial_Account_Balance} "
    
    # I want to make the actual withdraw section where it can use deposited balance to subtract the old 
    
    def Withdraw(self):
        Bank.Initial_Account_Balance = float(Bank.fund) - float(Bank.withdraw)  
        return f"Dear Esteemed Customer, you have N{Bank.Initial_Account_Balance} left. Thanks for Banking with us!"
            
       
   
User1 = Bank(name, age, LGA, State_of_origin, State_of_Residence, address, Nationality, Bank.fund, Bank.withdraw )


# print(User1.Deposit())
Bank.Initial_Account_Balance = 0.0
print(User1.Withdraw())


          
   

    


