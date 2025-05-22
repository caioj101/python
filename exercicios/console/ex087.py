matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)

maior = matriz[1][0]

for l in range(0, 3):
    soma += matriz[l][2]
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')