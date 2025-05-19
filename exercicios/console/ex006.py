import math
from cores import colorir

print(f'{colorir("DOBRO, TRIPLO E RAIZ QUADRADA >>>>>>>>>>", cor="verde", estilo="negrito")}')


n = int(input('Digite um número: '))
print(f'O dobro de {colorir(n, cor="magenta", estilo="negrito")} vale {colorir(n*2, cor="verde")}.\n'
f'O triplo de {colorir(n, cor="magenta", estilo="negrito")} vale {colorir(n*3, cor="verde", estilo="negrito")}.\n'
f'A raiz quadrada de {colorir(n, cor="magenta", estilo="negrito")} é igual a {colorir(f"{math.sqrt(n):.2f}", cor="verde", estilo="negrito")}.\n')
