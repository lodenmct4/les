def bereken_som(getal1, getal2):
    som= getal1 + getal2
    return som

def print_som(getal1,getal2):
    print(getal1+getal2)

def is_even (getal):
    if getal % 2 ==0:
        return True
    else : return False

som = bereken_som(4,9)
print (som)
print(bereken_som(78,978))

if is_even(78):
    print ("78 is even.")
else: print("78 is oneven.")