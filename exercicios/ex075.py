par = 0
numeros = (int(input('Digite um numero: ')),
int(input('Digite outro numero: ')),
int(input('Digite mais um numero: ')),
int(input('Digite o ultimo numero: ')))


for c in numeros:
    if c % 2 == 0:
        par += 1

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram {par}')
