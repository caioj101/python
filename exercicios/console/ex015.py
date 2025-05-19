from cores import colorir

print(f'{colorir("ALUGUEL DE CARROS >>>>>>>>>>", cor="verde", estilo="negrito")}')

dias = int(input('Quantos dias alugado? '))
km = int(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${colorir(f"{total:.2f}", cor="verde", estilo="negrito")}')
