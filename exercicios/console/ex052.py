contador = 0

n = int(input('Digite um número: '))

for c in range(1, n+1):
    if n % c == 0:
        contador += 1
        print(f'\033[0;33m{c}\033[m', end=' ',)
    else:
        print(f'\033[0;31m{c}\033[m', end=' ',)
               
print(f'\nO numero {n} foi divisível {contador} vez(es).')
if contador > 2:
    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
