
def cel_to_fah(value):
    fah = (value * 9/5) + 32
    fah = round(fah, 1)
    return fah
    

def fah_to_cel(value):
    cel = (value - 32) * 5/9
    cel = round(cel, 1)
    return cel

fah = cel_to_fah(3)
cel = fah_to_cel(100)
print(fah)
print(cel)
