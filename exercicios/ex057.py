sexo = input('Informe seu sexo: [M/F]: ').upper().strip()[0]
while sexo not in ('M', 'F'):
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')
 
 
# "Enquanto sexo não estiver dentro da tupla ('M', 'F'), continue perguntando"

#'M' in ('M', 'F') → True

#'F' in ('M', 'F') → True

#'X' in ('M', 'F') → False → o loop continua