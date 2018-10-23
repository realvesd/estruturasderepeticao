codigo = 5
valortotal = 0.00
quantidade = 0

menu = '''CÓDIGO 1 = Caderno - R$ 12.00;
	CÓDIGO 2 = Régua - R$ 2.50;
	CÓDIGO 3 = Borracha - R$ 0.25;
	CÓDIGO 4 = Mochila - R$ 50.00;
  0 - SAIR'''

while codigo != 0
  codigo = int(input("Informe o codigo do produto: "))
  if codigo == 1:
		valor = 12.00
	elif codigo == 2:
		valor = 2.50
	elif codigo == 3:
		valor = 0.25
	elif codigo == 4:
		valor = 50.00
	else:
		valor = 0.00
	
	if codigo > 0 and codigo < 5:
		quantidade = int(input("\nDigite a quantidade adquirida: "))
	else:
		quantidade = 0
	
	valor_total = (valor_total + (valor * quantidade))
print("O total da compra foi de R$",valortotal)
