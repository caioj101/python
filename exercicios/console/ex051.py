
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(0, 10):
    atual = p + c * r
    print(f'{atual}', end=' -> ')
print('Acabou', end='')
