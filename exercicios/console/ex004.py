from cores import colorir

print(f'{colorir("DISSECANDO UMA VARIÁVEL >>>>>>>>>>", cor="verde", estilo="negrito")}')

n = input('Digite algo: ')

teste = [
('Só tem espaços?', n.isspace()),
('É númerico?', n.isnumeric()),
('É alfabético? ', n.isalpha()),
('É alfanumérico? ', n.isalnum()),
('Está em maiúsculas? ', n.isupper()),
('Está em minúsculas? ', n.islower()),
('Está capitalizada? ', n.istitle())]

print(f'O tipo primitivo dessa valor é {colorir(type(n), cor="amarelo", estilo="negrito")}')
for pergunta, resultado in teste:
    if resultado == True:
        print(f'{pergunta} {colorir(resultado, cor="verde", estilo="negrito")}')
    else:
        print(f'{pergunta} {colorir(resultado, cor="vermelho", estilo="negrito")}')



