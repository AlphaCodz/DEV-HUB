
class Security:
    
    dangerous_words = ['']
    print("Hello! GoodDay, I am Sultan the head of security for this building for today")
    
    name = input("What is your name:: ")
    gender = input("Gender_[M/F]:: ")
    
    if gender.upper() == "M":
        print("Welcome Mr " + name)
    else:
        print("Welcome Mrs " + name)
        
    purpose = input("What is your purpose for being here? ")
    
    hold_on = "Please Give me a moment! i want to inform my boss of your arrival"
    print(hold_on)