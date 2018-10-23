preco1 = 0
cont = 0
for cont in range (0,10):
	preco = float(input("Digite o preço:"))
	if (preco > preco1):
		preco1 = preco

print("O maior preço foi de: ",preco1)
