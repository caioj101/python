valores = []
posicaomax = []
posicaomin = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 20)

maiorvalor = max(valores)
menorvalor = min(valores)

for pos, valor in enumerate(valores):
    if maiorvalor == valor:
        posicaomax.append(pos)
    elif menorvalor == valor:
        posicaomin.append(pos)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maiorvalor} na posição {posicaomax}')
print(f'O menor valor digitado foi {menorvalor} na posição {posicaomin}')

    