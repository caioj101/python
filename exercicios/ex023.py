n = int(input('Informe um número: '))
print(f'Analisando o número {n}')

#milhar
mil = n // 1000
resto1 = n % 1000

#centena
cento = resto1 // 100
resto2 = resto1 % 100

#dezena
dezena = resto2 // 10
resto3 = resto2 % 10

#unidade
unidade = resto3 

print(f'Unidade: {unidade:}')
print(f'Dezena: {dezena}')
print(f'Centena: {cento}')
print(f'Milhar: {mil}')
