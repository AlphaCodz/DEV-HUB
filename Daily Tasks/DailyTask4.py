# INPUT LENGTH CHECKER

# CONDITIONS

# If name is less than 3 characters long
# display message NAME MUST BE AT LEAST 3 CHARACTERS 

# otherwise if its more than 50 characters long
# display message NAME CAN BE A MAXIMUM OF 50 CHARACTERS

# otherwise 
# display message NAME LOOKS GOOD

name = input("Name:: ")

if len(name) < 3:
    print("Name Must be at least 3 characters")
    
elif len(name) > 50:
    print("Name must be a Maximum of 50 Characters")
    
else:
    print("Name Look's Good!")