from cores import colorir

print(f'{colorir("QUEBRANDO UM NÚMERO >>>>>>>>>>", cor="verde", estilo="negrito")}')

from math import floor as arredonda
n = float(input('Digite um valor: '))
print(f'O valor digitado foi {colorir(f"{n:.2f}", cor="magenta", estilo="negrito")} e a sua porção inteira é {colorir(f"{arredonda(n)}", cor="magenta", estilo="negrito")}')
