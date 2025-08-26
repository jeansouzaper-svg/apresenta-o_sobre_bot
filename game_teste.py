from time import sleep
import sys
from rich import print as rprint

def print_texto_lento(texto, atraso_letra=0.05, atraso_linha=1):
    """
    Imprime uma string letra por letra com um atraso.
    """
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        sleep(atraso_letra)
    print()
    sleep(atraso_linha)

def primeira_pergunta():
    """
    Função para apresentar a primeira pergunta e reagir à escolha.
    """
    # Usamos print_texto_lento para exibir as perguntas e opções
    print_texto_lento("Devemos xingar o aluno? ")
    print_texto_lento("1- Sim, Devemos! ")
    print_texto_lento("2- Não, não podemos! ")

    # Captura a entrada do usuário
    opcao = input("Escolha a opção escrevendo 1 ou 2: ")

    # Verifica a opção e imprime o resultado
    if opcao == "1":
        print_texto_lento("Você está demitido! ")
    elif opcao == "2":
        print_texto_lento("Parabéns, você vai seguir para o proximo dia! ")
    else:
        print_texto_lento("Não existe meio termo, você tem que escolher! ")

def main():
    """
    Função principal que organiza a ordem das ações.
    """
    # 1. Mensagem de boas-vindas
    nome = input("Insira o seu nome: ")
    linha_boas_vindas = f"Bem vindo(a) {nome}"
    
    linhas = [
        linha_boas_vindas,
        "Hoje você está prestes a se aventurar sobre a condução de atendimento"
    ]

    for linha in linhas:
        print_texto_lento(linha)
    
    # 2. Pergunta de múltipla escolha
    primeira_pergunta()

if __name__ == "__main__":
    main()