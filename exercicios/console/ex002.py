from cores import colorir

print(f'{colorir('RESPONDENDO AO USUÁRIO >>>>>>>>>>', cor="verde", estilo="negrito")}')

nome = input('Digite o seu nome: ')
print(f'É um prazer te conhecer, {colorir(nome, cor="verde", estilo="negrito")}!')
