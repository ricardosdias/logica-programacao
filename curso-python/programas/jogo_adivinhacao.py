import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = int(input("Tente adivinhar o número (entre 1 e 100): "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("O número é maior. Tente novamente!")
        else:
            print("O número é menor. Tente novamente!")

jogo_adivinhacao()