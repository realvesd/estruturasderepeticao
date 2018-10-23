menor15 = 0
maior15 = 0

while idade >= 0:
  idade = int(input("Informe uma idade: "))
  if idade <= 15 and idade > 0:
    menor15 +=1
  elif idade > 15 and idade >0:
    maior15 +=1

print("A quantidade de pessoas da primeira faixa etaria foi ", menor15 "pessoas, e da segunda faixa etaria ", maior15, "pessoas")
