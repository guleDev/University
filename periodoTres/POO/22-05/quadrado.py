import pygame
import sys

pygame.init()

# Definir as dimensões da janela
largura = 640
altura = 480

# Cria Janela
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela
pygame.display.set_caption('Janela Interativa Pygame')

# Define cores
cor_fundo = (0, 120, 120) # Azul esverdeado
cor_retangulo = (255, 255, 255) # Branco
cor_fundo_nova = (120, 0, 120) # Roxo

# Posição inicial do retângulo
pos_x = largura // 2
pos_y = largura // 2

# Tamanho do retângulo
ret_largura = 60
ret_altura = 40

# Velocidade de movimento do retângulo
velocidade = 5

# Loop principal do jogo
rodando = True

while rodando:
    # Verifica todos os eventos do jogo
    for evento in pygame.event.get():
        # Se o evento for um pedido para fechar a janela
        if evento.type == pygame.QUIT:
            rodando = False
        # Se uma tecla for precionada
        elif evento.type == pygame.KEYDOWN:
            # Muda a cor de fundo se a tecla 'c' for precionada
            if evento.key == pygame.K_c:
                cor_fundo = cor_fundo_nova

    # Verifica teclas precionadas para mover o retângulo
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pos_x -= velocidade
    if teclas[pygame.K_RIGHT]:
        pos_x += velocidade
    if teclas[pygame.K_UP]:
        pos_y -= velocidade
    if teclas[pygame.K_DOWN]:
        pos_y += velocidade
    
    # Preenche a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenha um retângulo na tela
    pygame.draw.rect(tela, cor_retangulo, (pos_x, pos_y, ret_largura, ret_altura))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
sys.exit()
