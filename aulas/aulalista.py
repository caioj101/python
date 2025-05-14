num=[2, 5, 9, 1] # criando a lista
num[2]= 3 # trocando o número 9 por 3
num.append(7)# adicionando algo ao final da lista
num.sort()# colocando em ordem os números
num.sort(reverse=True)# mostrando o reverso da lista
num.insert(2, 0) # Na posição 2 inserir o valor 0
num.pop() # exlui o ultimo elemento da lista
num.pop(2) # exclui o elemento 2 da lista
if 8 in num:
    num.remove(8)
else:
    print('Não achei o número 8')
print(num)
print(f'Essa lista tem {len(num)} elementos') # mostrando a quantidade de elemntos da lista

#CRIANDO OUTRA LISTA MAIS ORGANIZADA
valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate (valores):
    print(f'Na posição {c}, encontrei o valor {v} !')
print('cheguei ao final da lista')
#LENDO VALORES PELO TECLADO
valor=list()
for cont in range(0,5):
    valor.append(int(input('digite um valor: ')))
for pos, d in enumerate (valor):
    print(f'Na posição {pos}, encontrei o valor {d}')
# JUNTANDO DUAS LISTAS
a=[1,5,7,1]
b=a
b[2]=5 # vai trocar o valor das duas listas
#b = a[:] b clona os valores de a, mas agora podendo mexer só com os valore de b
print(f'Lista a: {a}')
print(f'Lista b: {b}')