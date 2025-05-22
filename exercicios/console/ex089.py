dadoaluno = []
aluno = []
while True:
    dadoaluno.append(str(input('Nome: ')))
    dadoaluno.append(float(input('Nota 1: ')))
    dadoaluno.append(float(input('Nota 2: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    aluno.append(dadoaluno[:])
    dadoaluno.clear()
    while resp not in ['s', 'n']:
        print('Dado inválido! Tente novamente.')
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print('-=' * 30)
print('No.\tNOME\tMÉDIA')
print('-' * 30)
for i, l in enumerate(aluno):
    print(f'{i}\t{l[0]}\t{(l[1]+l[2]) / 2:.1f}')
print('-' * 30)

while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    print('-' * 30)
    print(f'Notas de {aluno[notas][0]} são {aluno[notas][1]}, {aluno[notas][2]}')
    print('-' * 30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
