cores = {
    # Reset
    'limpa': '\033[0m',

    # Cores de texto (foreground)
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'magenta': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Fundos (background)
    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_magenta': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',

    # Estilos
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'inverso': '\033[7m',
}

def colorir(texto, cor=None, fundo=None, estilo=None):
    codigo = ''
    if estilo in cores:
        codigo += cores[estilo]
    if cor in cores:
        codigo += cores[cor]
    if fundo in cores:
        codigo += cores[fundo]
    return f"{codigo}{texto}{cores['limpa']}"
