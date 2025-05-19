tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro' )

for palavras in tupla:
    encontradas = []
    for vogais in palavras:
        if vogais in 'aeiou':
            encontradas.append(vogais)
    print(f'Na palavra {palavras} temos {", ".join(encontradas)}')