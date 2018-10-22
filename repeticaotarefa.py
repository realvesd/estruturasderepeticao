codigo = "sim"
while codigo != "nao" and codigo == "sim":
	distancia = float(input("Informe a distância percorrida pelo atleta: "))
	tempo = float(input("Informe o tempo levado para percorrer essa distância: "))
	
	velocidade = distancia/tempo

	print("A velocidade do atleta foi de",velocidade,"metros por segundo.")
	codigo = input("Deseja continuar a executar o programa?")

if codigo != "sim" and codigo != "nao"
	print("COMANDO INVÁLIDO!")
