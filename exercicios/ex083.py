exp = []
lista = [] 

exp.append(str(input('Digite uma expressão: ')))

for letras in exp:
    if letras == '(':
        lista.append('(')
    elif letras == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
        

if len(lista) == 0:
    print('A sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
