
def company(wkr1, wkr2, wkr3):
    rnk1 = 0
    rnk2 = 0
    rnk3 = 0
    sal1 = 0
    sal2 = 0
    sal3 = 0
    salary = 30000
    wkr1 = wkr1.split(" ")
    wkr2 = wkr2.split(" ")
    wkr3 = wkr3.split(" ")
    
    rnk1 = int(wkr1[1])
    rnk2 = int(wkr2[1])
    rnk3 = int(wkr3[1])
    
    sal1 = ((rnk1 * 0.5) * salary)
    sal2 = ((rnk2 * 0.5) * salary)
    sal3 = ((rnk3 * 0.5) * salary)
    
    msg = wkr1[0] + " at rank " + wkr1[1] + ",  have been credited N" + str(sal1)
    print(msg)
    msg = wkr2[0] + " at rank " + wkr2[1] + ",  have been credited N" + str(sal2)
    print(msg)
    msg = wkr3[0] + " at rank " + wkr3[1] + ",  have been credited N" + str(sal3)
    print(msg)
