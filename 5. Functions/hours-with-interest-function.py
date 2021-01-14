#program calculates the payment by hours worked with the interest by overtime

#function to calculate
def computepay(hour, rate) :
    #verify if hours worked is less than 40 ou higher, if higher, applys the interest
    if hour <= 40 :
        total = hour * rate
        payment = total * overtime
    else : 
        payment = 40 * rate + (hour - 40) * rate * 1.5
	return payment
    
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

#calls function
result = computepay(hourFloat, rateFloat)

#show the total
print("Pay",result)