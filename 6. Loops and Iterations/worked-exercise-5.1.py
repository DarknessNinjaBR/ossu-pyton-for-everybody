numberQtd = 0
total = 0

#loop that users insert the numbers, if write done, the loop stops
while True
    numberInput = input("Insira um numero:")
    if numberInput == "done" :
        break
    try:
        numberFloat = float(numberInput)
    except:
        print("Valor invalido")
        continue

    #calculate the number quantity and the total of sum
    numberQtd = numberQtd + 1
    total = total + numberFloat

#print total, number quantity and the average
print("O total é:"+total,", o a quantidade de numeros inseridos é:"+numberQtd,"e a média é:"total/numberQtd)