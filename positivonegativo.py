cont = 0

for cont in range (0,10):
	numero = int(input("Digite um número:"))
	numero = numero*3
	print("O triplo desse número é",numero)
	if (numero >= 0):
		print("É positivo!")
	else:
		print("É negativo!")	
