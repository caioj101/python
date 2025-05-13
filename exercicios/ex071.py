n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
resto = 0

print('=' * 20)
print(f'{"BANCO CSC":^20}')
print('=' * 20)

dinheiro = int(input('Que valor você quer sacar? R$'))

if dinheiro >= 50:
    n50 = dinheiro // 50
    resto = dinheiro % 50
if resto >= 20:
    n20 = resto // 20
    resto = resto % 20
if resto >= 10:
    n10 = resto // 10
    resto = resto % 10
if resto >= 1:
    n1 = resto // 1
    
if n50 > 0:
    print(f'Total de {n50} cédula(s) de R$50')
if n20 > 0:
    print(f'Total de {n20} cédula(s) de R$20')
if n10 > 0:
    print(f'Total de {n10} cédula(s) de R$10')
if n1 > 0:
    print(f'Total de {n1} cédula(s) de R$1')

print('=' * 20)

print('Volte sempre ao BANCO CSC! Tenha um bom dia!')
