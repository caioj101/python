dado = {}

dado['Nome'] = str(input('Nome: '))
dado['Media'] = float(input(f'Média de {dado["Nome"]}: '))
if dado['Media'] >= 7:
    dado['Situacao'] = 'Aprovado'
elif dado['Media'] >= 5:
    dado['Situacao'] = 'Recuperação'
else:
    dado['Situacao'] = 'Reprovado'


for k, v in dado.items():
    print(f'- {k} é igual a {v}')
        
            