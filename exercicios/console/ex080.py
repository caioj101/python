valores = []

for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(valores) == 0:
        valores.append(num)
        print(f'Valor adicionado ao final da lista')
    else:
        inserido = False                  #criar uma variavel e definir como falso, flag
        for pos, n in enumerate(valores): #para cada posição e numero em valores:
            if num < n:                   #se num for menor que n                    
                valores.insert(pos, num)  #inserir num na posição pos
                inserido = True           #marca inserido como verdadeiro
                print(f'Adicionado na posição {pos} da lista...')
                break                     # e para o laço
        if inserido == False:             #se inseriso ainda for falso
            valores.append(num)           #adicionar num ao final da lista
            print(f'Valor adicionado na posição {len(valores) - 1} da lista...')
print(valores)
