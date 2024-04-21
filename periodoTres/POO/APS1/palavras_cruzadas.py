import json
import random
import time

def carregar_palavras():
    with open("palavras_cruzadas.json", "r") as file:
        return json.load(file)

def salvar_palavras(palavras_cruzadas):
    with open("palavras_cruzadas.json", "w") as file:
        json.dump(palavras_cruzadas, file, indent=2)

def jogar(palavra, dicas):
    print(f"Dica 1: {dicas[0]} ( {len(palavra) * '_ '})")
    palpite = input("Sua resposta: ")

    if palpite.lower() == palavra:
        print("Correto!")
        return True
    else:
        for i in range(1, len(dicas)):
            print(f"Dica {i + 1}: {dicas[i]}")
            palpite = input("Sua próxima tentativa: ")
            if palpite.lower() == palavra:
                print("Correto!")
                return True
        print(f"Incorreto! A resposta correta é '{palavra}'.")
        return False

def calcular_pontuacao(tempo_decorrido, tentativas, resposta_correta):
    if tentativas == 0:  # Resposta correta na primeira tentativa
        return 10
    elif tentativas == 1:  # Resposta correta na segunda tentativa
        return 5
    else:  # Resposta correta após duas tentativas ou mais
        return 2

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

def main():
    palavras_cruzadas = carregar_palavras()

    print("Bem-vindo ao jogo de palavras cruzadas!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Jogador Único")
        print("2. Multijogador")
        print("3. Modo de Estudo")
        print("4. Adicionar Palavra")
        print("5. Sair")
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
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
                    pontuacao += calcular_pontuacao(time.time() - start_time, 0, palavra)
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Sua pontuação final é: {pontuacao}")
            print(f"Tempo total: {total_time:.2f} segundos")
            
        elif opcao == '2':
            print("\nEscolha o nível de dificuldade:")
            print("1. Fácil")
            print("2. Médio")
            print("3. Difícil")
            nivel_opcao = input("Digite o número da opção desejada: ")
            niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
            nivel = niveis.get(nivel_opcao)
            
            print(f"\nNível selecionado: {nivel.capitalize()}")

            jogadores = int(input("Digite o número de jogadores: "))
            pontuacoes = {jogador: 0 for jogador in range(1, jogadores + 1)}

            for jogador in range(1, jogadores + 1):
                print(f"\nJogador {jogador}, é sua vez.")
                palavras_selecionadas = random.sample(list(palavras_cruzadas[nivel].items()), 3)
                start_time = time.time()
                for palavra, dicas in palavras_selecionadas:
                    if jogar(palavra, dicas):
                        pontuacao = calcular_pontuacao(time.time() - start_time, 0, palavra)
                        pontuacoes[jogador] += pontuacao
                    else:
                        print("Você não acertou a palavra.")
                        print(f"A resposta correta é: {palavra}")

                end_time = time.time()
                total_time = end_time - start_time
                print(f"Pontuação do jogador {jogador}: {pontuacoes[jogador]}")
                print(f"Tempo total: {total_time:.2f} segundos")

        elif opcao == '3':
            print("\nEscolha o nível de dificuldade:")
            print("1. Fácil")
            print("2. Médio")
            print("3. Difícil")
            nivel_opcao = input("Digite o número da opção desejada: ")
            niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
            nivel = niveis.get(nivel_opcao)
            
            print(f"\nNível selecionado: {nivel.capitalize()}")

            estudar(palavras_cruzadas, nivel)
            
        elif opcao == '4':
            print("\nEscolha o nível de dificuldade:")
            print("1. Fácil")
            print("2. Médio")
            print("3. Difícil")
            nivel_opcao = input("Digite o número da opção desejada: ")
            niveis = {"1": "fácil", "2": "médio", "3": "difícil"}
            nivel = niveis.get(nivel_opcao)
            
            print(f"\nNível selecionado: {nivel.capitalize()}")

            adicionar_palavra(palavras_cruzadas, nivel)

        elif opcao == '5':
            print("Obrigado por jogar! Até mais!")
            salvar_palavras(palavras_cruzadas)
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
