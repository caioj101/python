nome = input('Digite seu nome completo: ').strip
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
primeiro = nome.split()
junto = ''.join(nome.split())
print(f'Seu nome tem ao todo {len(junto)} letras')
print(f'Seu primeiro nome é {primeiro[0]} e ele tem {len(primeiro[0])}')