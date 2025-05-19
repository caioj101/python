soma = 0
contador = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        contador += 1

print(f'A soma dos {contador} valores pares é {soma}')
