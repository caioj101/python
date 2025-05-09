tot = 1
n = int(input('Digite um número para calcular o seu fatorial: '))
print(f'Calculando {n}! = ', end='')
while n >= 1:
    print(f'{n} ', end='')
    if n > 1:
        print(end='x ')
    tot *= n
    n -= 1
print(f'= {tot}')
