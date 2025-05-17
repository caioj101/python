from cores import colorir

print(f'{colorir("CONVERSOR DE TEMPERATURAS >>>>>>>>>>", cor="verde", estilo="negrito")}')

celcius = float(input('Informe a temperatura em °C: '))
f = celcius * 1.8 + 32
print(f'A temperatura de {colorir(celcius, cor="magenta", estilo="negrito")}°C corresponde a {colorir(f, cor="verde", estilo="negrito")}°F')
