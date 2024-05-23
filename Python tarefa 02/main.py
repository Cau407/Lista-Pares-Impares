lista = []
numero = 0
pares = []
impares = []


while numero < 10:
    lista.append(int(input("Digite um valor pra adicionar na lista: ")))
    numero += 1

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

paresTupla = tuple(pares)
imparesTupla = tuple(impares)

print(f"Os números pares são {paresTupla}")
print(f"Os números ímpares são {imparesTupla}")
print(f"A sua lista tem {len(pares)} números pares!")
print(f"A sua lista tem {len(impares)} números ímpares!")
print(f"A soma dos números pares é: {sum(pares)}")
print(f"A soma dos números ímpares é: {sum(impares)}")