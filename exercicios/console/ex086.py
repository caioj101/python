matriz = []


for linha in range(0, 3):
    linha_temp = []
    for coluna in range(0, 3):
        valor = int(input(f'Digite um número para a linha {linha} e posição {coluna}: '))
        linha_temp.append(valor)
    matriz.append(linha_temp)
    
print('=-' * 30)

for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()
