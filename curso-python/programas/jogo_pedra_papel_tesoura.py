import random
from enum import Enum


class Escolha(Enum):
    PEDRA = 'pedra'
    PAPEL = 'papel'
    TESOURA = 'tesoura'


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return 'Empate'
    elif (jogador == Escolha.PEDRA and computador == Escolha.TESOURA) or \
         (jogador == Escolha.PAPEL and computador == Escolha.PEDRA) or \
         (jogador == Escolha.TESOURA and computador == Escolha.PAPEL):
        return 'Jogador'
    else:
        return 'Computador'


def jogo_pedra_papel_tesoura():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")

    while True:
        opcoes = list(Escolha)
        escolha_computador = random.choice(opcoes)
        escolha_jogador = input(
            "Escolha Pedra, Papel ou Tesoura (ou 'sair' para terminar): ").lower()

        if escolha_jogador == 'sair':
            break

        if escolha_jogador not in Escolha._value2member_map_:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_jogador = Escolha(escolha_jogador)
        print(
            f"Você escolheu {escolha_jogador.value}, o computador escolheu {escolha_computador.value}.")

        vencedor = determinar_vencedor(escolha_jogador, escolha_computador)
        if vencedor == 'Empate':
            print("É um empate!")
        else:
            print(f"O {vencedor} vence!")


if __name__ == "__main__":
    jogo_pedra_papel_tesoura()
