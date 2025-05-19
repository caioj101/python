valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    while resp not in ['s', 'n']:
        print('Dado inválido. Tente novamente! ', end='')
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
    if resp == 'n':
        break

for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
        
print('=-' * 20)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
