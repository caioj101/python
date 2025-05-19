from math import hypot

opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(opo, adj):.2f}')
