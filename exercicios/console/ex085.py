numeros = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
    

print('-=' * 30)
print(numeros)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
 