soma = 0
contador = 0

for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
            contador += 1
print(f'A soma de todos os {contador} valores solicitados é {soma}')
