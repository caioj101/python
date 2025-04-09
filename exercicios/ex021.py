pip install pygame

import pygame

# Inicializa todos os módulos do Pygame
pygame.init()

# Inicializa o sistema de vídeo para evitar erros, mesmo que não seja usada uma janela visível
pygame.display.set_mode((1, 1))

# Inicializa o mixer de som
pygame.mixer.init()

# Carrega e reproduz o arquivo de música
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

# Espera que a reprodução do som termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Encerra o Pygame corretamente
pygame.quit()
