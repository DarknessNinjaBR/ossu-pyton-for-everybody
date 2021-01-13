#calculates the score

#users insert the score
scoreInput = input("Insira o score: ")

#verify if is a number ou letters, and if not, quit application
try:
	scoreFloat = float(scoreInput)
except:
    print("Insira um valor válido")
    quit()

#verify if are a valid value    
if scoreFloat > 1:
    print("O valor deve ser maior que zero e menor ou igual a 1")
    quit() 
elif scoreFloat < 0:
    print("O valor deve ser maior que zero e menor ou igual a 1")
    quit() 
    
#calculate and show score
if scoreFloat >= 0.9:
    print("A")
elif scoreFloat >= 0.8:
    print("B")
elif scoreFloat >= 0.7:
    print("C")
elif scoreFloat >= 0.6:
    print("D")
elif scoreFloat > 0.6:
    print("F")