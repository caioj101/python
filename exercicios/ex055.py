peso = float(input('Peso da 1° pessoa: '))
menor = peso
maior = menor
 
for c in range(2, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso
        
print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')