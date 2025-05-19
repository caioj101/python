total = 0
maior = 0
alunos = 0
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nota = float(input('nota: '))
    total += nota
    if nota > maior:
        maior = nota
        maiornota = nome
    if idade < 18 and nota > 7:
        alunos += 1

media = total / 4

print(f'A média de nota do grupo é de {media:.1f}')
print(f'O aluno com maior nota é {maior:.1f} e se chama {maiornota}')
print(f'Ao todo são {alunos} alunos com menos de 18 anos e nota maior que 7')
