import time
import random

def efeito_digi(texto, velocidade=0.05):
    """Imprime texto com efeito de digitação."""
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()

def introducao():
    """Mostra a introdução do jogo e pede o nome do personagem."""
    print("[===|Projeto Fallout New Austin. V.0.0.1. Pre-Alpha|===]")
    print("[==========|Bem Vindo|]")
    nome = input('[==========|Insira o Nome do Seu Personagem:  ')
    print(f"[==========|Olá {nome}! Seja Bem Vindo ao Fallout New Austin|]")
    return nome

def menu_principal(nome):
    """Menu inicial para continuar ou sair."""
    while True:
        print("[==========|Deseja continuar a experiência ?|]")
        print("a. Sim.")   
        print("b. Não.")
        escolha = input(": ")

        if escolha == 'b':
            efeito_digi(f"{nome} fez sua escolha.....Até Mais.", 0.1)
            break
        elif escolha == 'a':
            jogar(nome)

def jogar(nome):
    """Executa uma rodada do jogo com perguntas aleatórias."""
    perguntas = [
        'Saindo do Vault você encontrou uma cidade abandonada, Thumbleweed. Você entra?',
        'Saindo do Vault você acaba ficando sem comida e água. Você continua andando?',
        'Saindo do Vault um estranho se aproxima de você com uma arma. Você confia nele?',
        'Saindo do Vault você encontrou um terminal de computador bloqueado. Você tenta hackear?',
        'Saindo do Vault 7 você encontra outro Vault, o Vault 49. Você entra?',
        'Saindo do Vault você encontrou um grupo de sobreviventes hostis, os El Lobos. Você tenta negociar?',
        'Saindo do Vault você encontrou uma arma poderosa, mas pesada. Você a leva?',
        'Saindo do Vault você tem a chance de se juntar a uma facção, os Mcqueens. Você se junta?',
        'Saindo do Vault você encontrou um robô danificado. Você tenta consertá-lo?'
    ]
    pergunta = random.choice(perguntas)

    print('{==========|Então-se Prepare.|}')
    efeito_digi("{==========|Inicializando..........100%|}", 0.1)
    print('#', pergunta)

    while True:
        print("1.) Sim.")
        print("2.) Não.")
        escolha2 = input('Ação: ')

        if escolha2 == '2':
            efeito_digi(f"{nome} fez sua escolha.....Até Mais.", 0.1)
            break
        elif escolha2 == '1':
            print('#', pergunta)
            break

def main():
    """Função principal que inicia o jogo."""
    nome = introducao()
    menu_principal(nome)

# Executa o jogo
if __name__ == "__main__":
    main()
