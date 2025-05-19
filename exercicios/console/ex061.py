print('Gerador de PA')
print('-=' * 10)
n = 0

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

while n < 10:
    atual = p + n * r
    print(f'{atual}', end=' -> ')
    n +=1
print('FIM', end='')