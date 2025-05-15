from cores import colorir

print(f'{colorir("MÉDIA ARITMÉTICA >>>>>>>>>>", cor="verde", estilo="negrito")}')

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
print(f'A média entre {colorir(n1, cor="magenta", estilo="negrito")} e {colorir(n2, cor="magenta", estilo="negrito")} é igual a {colorir(f"{media:.1f}", cor="verde")}')
