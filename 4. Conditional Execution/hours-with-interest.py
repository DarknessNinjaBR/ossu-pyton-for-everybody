#program calculates the payment by hours worked with the interest by overtime

#user says hours
hourInput = input("Insira o numero de horas trabalhadas: ")

#user says the rate by the hour
rateInput = input("Insira o valor por cada hora trabalhada: R$")

#convert string to float and verify if user wrote letters
try:
    hourFloat = float(hourInput)
    rateFloat = float(rateInput)
except:
    print('Valor inserido não é um numero, aplicação fechada')
    quit()

#verify if hours worked is less than 40 ou higher, if higher, applys the interest
if hourFloat <= 40 :
    total = hourFloat * rateFloat
    payment = total * overtime
else : 
    payment = 40 * rateFloat + (hourFloat - 40) * rateFloat * 1.5

#show the total
print(payment)