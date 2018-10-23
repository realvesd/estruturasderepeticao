cont = 0
otimo = 0
bom = 0
regular = 0

for cont in range (0,5):
opiniao = int(input("Qual sua opinião sobre o filme? 3 - Otimo ,2 - Bom ou 3 - Regular"))
if opiniao == '3':
  otimo += 1
elif opiniao == '2':
  bom += 1
elif opiniao == '3':
  regular += 1
else:
  print("Opcao invalida!")

print("O numero de pessoas que achou o filme otimo foi: ", otimo,"as que acharam bom: ", bom, "e as que acharam regular: ", regular)
