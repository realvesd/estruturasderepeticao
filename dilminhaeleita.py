cont = 0
sim = 0
nao = 0
invalidos = 0

for cont in range (0,15):
	voto = str(input("Dilma será reeleita? Digite 1 para SIM e 2 para NAO"))
if voto == '1':
  sim += 1
elif voto == '2':
  nao += 1
else:
  invalidos += 1

print("O número de votos positivos foi: ", sim, "o de negativos: ", nao, "e o de inválidos: ", invalidos)
