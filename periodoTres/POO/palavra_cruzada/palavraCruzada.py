import pygame
import json
import random
import time

# Inicializar o Pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Palavras Cruzadas")

# Carregar palavras do arquivo JSON
def carregar_palavras():
    try:
        with open("palavras_cruzadas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}


# Salvar palavras no arquivo JSON
def salvar_palavras(palavras_cruzadas):
    with open("palavras_cruzadas.json", "w") as file:
        json.dump(palavras_cruzadas, file, indent=2)

# Função para jogar
def jogar(palavra, dicas):
    # Lógica para jogar
    print(f"Dica 1: {dicas[0]} ( {len(palavra) * '_ '})")
    palpite = input("Sua resposta: ")

    if palpite.lower() == palavra.lower():
        print("Correto!")
        return True
    else:
        for i in range(1, len(dicas)):
            print(f"Dica {i + 1}: {dicas[i]}")
            palpite = input("Sua próxima tentativa: ")
            if palpite.lower() == palavra:
                print("Correto!")
                return True
        return False

# Função para calcular pontuação
def calcular_pontuacao(tempo_decorrido, tentativas, resposta_correta):
    if tentativas == 0:  # Resposta correta na primeira tentativa
        return 10
    elif tentativas == 1:  # Resposta correta na segunda tentativa
        return 5
    else:  # Resposta correta após duas tentativas ou mais
        return 2

# Função para estudar
def estudar(palavras_cruzadas, nivel):
    print("Modo de estudo:")
    print("Você revisará três palavras aleatórias do nível selecionado.")
    print("Aqui estão as palavras e suas dicas:\n")
    
    palavras_estudo = random.sample(list(palavras_cruzadas[nivel].items()), 3)
    for palavra, dicas in palavras_estudo:
        print(f"Palavra: {palavra}")
        print("Dicas:")
        for i, dica in enumerate(dicas, start=1):
            print(f"{i}. {dica}")
        print()

# Função para adicionar palavra
def adicionar_palavra(palavras_cruzadas, nivel):
    palavra = input("Digite a palavra que deseja adicionar: ")
    if palavra in palavras_cruzadas[nivel]:
        print("Essa palavra já existe neste nível de dificuldade.")
    else:
        dicas = []
        print("Digite as dicas para a palavra:")
        for i in range(1, 3):
            dicas.append(input(f"Dica {i}: "))
        palavras_cruzadas[nivel][palavra] = dicas
        print(f"A palavra '{palavra}' foi adicionada com sucesso ao nível '{nivel}'.")

# Função para desenhar texto na tela
def desenhar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.SysFont(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    screen.blit(texto_surface, texto_rect)

# Função principal
def main():
    palavras_cruzadas = carregar_palavras()

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salvar_palavras(palavras_cruzadas)
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("\nEscolha o nível de dificuldade:")
                    print("1. Fácil")
                    print("2. Médio")
                    print("3. Difícil")
                    nivel_opcao = input("Digite o número da opção desejada: ")
                    niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
                    nivel = niveis.get(nivel_opcao)
                    
                    print(f"\nNível selecionado: {nivel.capitalize()}")
                    
                    print("\nPreencha as palavras cruzadas com as respostas corretas.")

                    start_time = time.time()
                    palavras_selecionadas = random.sample(list(palavras_cruzadas[nivel].items()), 3)
                    pontuacao = 0
                    for palavra, dicas in palavras_selecionadas:
                        if jogar(palavra, dicas):
                            pontuacao += calcular_pontuacao(0)
                    end_time = time.time()
                    total_time = end_time - start_time
                    print(f"Sua pontuação final é: {pontuacao}")
                    print(f"Tempo total: {total_time:.2f} segundos")

                elif event.key == pygame.K_2:
                    print("\nEscolha o nível de dificuldade:")
                    print("1. Fácil")
                    print("2. Médio")
                    print("3. Difícil")
                    nivel_opcao = input("Digite o número da opção desejada: ")
                    niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
                    nivel = niveis.get(nivel_opcao)
                    
                    print(f"\nNível selecionado: {nivel.capitalize()}")

                    estudar(palavras_cruzadas, nivel)
                    
                elif event.key == pygame.K_3:
                    print("\nEscolha o nível de dificuldade:")
                    print("1. Fácil")
                    print("2. Médio")
                    print("3. Difícil")
                    nivel_opcao = input("Digite o número da opção desejada: ")
                    niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
                    nivel = niveis.get(nivel_opcao)
                    
                    print(f"\nNível selecionado: {nivel.capitalize()}")

                    adicionar_palavra(palavras_cruzadas, nivel)

                elif event.key == pygame.K_4:
                    print("Obrigado por jogar! Até mais!")
                    salvar_palavras(palavras_cruzadas)
                    pygame.quit()
                    return

        # Limpar a tela
        screen.fill(WHITE)

        # Desenhar menu
        desenhar_texto("Bem-vindo ao Jogo de Palavras Cruzadas!", 40, BLACK, WIDTH // 2, 100)
        desenhar_texto("Escolha uma opção:", 30, BLACK, WIDTH // 2, 200)
        desenhar_texto("1. Jogar", 30, BLACK, WIDTH // 2, 250)
        desenhar_texto("2. Estudar", 30, BLACK, WIDTH // 2, 300)
        desenhar_texto("3. Adicionar Palavra", 30, BLACK, WIDTH // 2, 350)
        desenhar_texto("4. Sair", 30, BLACK, WIDTH // 2, 400)

        # Atualizar a tela
        pygame.display.flip()

if __name__ == "__main__":
    main()
