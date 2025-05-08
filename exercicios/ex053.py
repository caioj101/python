frase = input('Digite uma frase: ').strip().upper().replace(' ', '')
invertido = (frase[::-1])
print(f'O inverso de {frase} é {invertido}')
if frase == invertido:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

