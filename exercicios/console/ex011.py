from cores import colorir

print(f'{colorir("PINTANDO PAREDES >>>>>>>>>>", cor="verde", estilo="negrito")}')

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
tinta = area / 2

print(f'Sua parede tem a dimensão de {colorir(lar, cor="vermelho", estilo="negrito")} x {colorir(alt, cor="vermelho", estilo="negrito")} e sua área é de {colorir(f"{area:.2f}", cor="verde", estilo="negrito")}m².')
print(f'Para pintar essa parede, você precisará de {colorir(tinta, cor="verde", estilo="negrito")}l de tinta.')
