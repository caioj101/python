from cores import colorir

print(f'{colorir("CALCULANDO DESCONTOS >>>>>>>>>>", cor="verde", estilo="negrito")}')

preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - (preco * 5 / 100)
print(f'O produto que custava R${colorir(f"{preco:.2f}", cor="magenta", estilo="negrito")}, na promoção com desconto de {colorir("5%", cor="verde", estilo="negrito")} vai custar R${colorir(f"{desconto:.2f}", cor="verde", estilo="negrito")}')
