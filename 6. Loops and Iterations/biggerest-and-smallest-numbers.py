total = 0
smallest = None
biggest = None

while True :
    numberInput = input("Enter a number: ")
    if numberInput == "done" :
        break
    try : 
        numberFloat = float(numberInput)
        #verify if biggest is none, if is, add the current value, else, verify if number is greater and trade
        if biggest is None :
            biggest = numberFloat
        elif biggest < numberFloat :
            biggest = numberFloat
        #verify if smallest is none, if is, add the current value, else, verify if number is less and trade
        if smallest is None :
            smallest = numberFloat
        elif smallest > numberFloat :
            smallest = numberFloat
    except :
        #if insert letters, show error mensage
        print("Invalid input")
        continue

#print biggest and smallest values
print("Maximum is",int(biggest))
print("Minimum is",int(smallest))