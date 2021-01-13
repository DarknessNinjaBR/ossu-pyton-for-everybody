#program calculates the payment by hours worked

#user says hours
hourInput = input("Insira o numero de horas trabalhadas")

#user says the rate by the hour
rateInput = input("Insira o valor por cada hora trabalhada: R$")

#multiplicate the hour with rate
total = float(hourInput) * float(rateInput)

#show the total of payment
print("Pay:", total)
