from cores import colorir

print(f'{colorir("CONVERSOR DE MEDIDAS >>>>>>>>>>", cor="verde", estilo="negrito")}')

m = float(input('Uma distância em metros: '))
print(f'A medida de {colorir(f"{m:.0f}", cor="magenta", estilo="negrito")}m corresponde a:')
print(f'{colorir(m/1000, cor="verde", estilo="negrito")}km')
print(f'{colorir(m/100, cor="verde", estilo="negrito")}hm')
print(f'{colorir(m/10, cor="verde", estilo="negrito")}dam')
print(f'{colorir(f"{m*10:.0f}", cor="verde", estilo="negrito")}dm')
print(f'{colorir(f"{m*100:.0f}", cor="verde", estilo="negrito")}cm')
print(f'{colorir(f"{m*1000:.0f}", cor="verde", estilo="negrito")}mm')
