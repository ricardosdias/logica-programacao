# Programa de Quiz sobre Precedência de Operadores em Python

def fazer_pergunta(pergunta, alternativas, resposta_correta):
    print(pergunta)
    for i, alternativa in enumerate(alternativas):
        print(f"{i + 1}. {alternativa}")

    resposta_usuario = input("Escolha a alternativa correta (1/2/3/4): ")

    if resposta_usuario.isdigit() and int(resposta_usuario) - 1 == resposta_correta:
        print("Correto!\n")
        return True
    else:
        print(
            f"Errado! A resposta correta é: {alternativas[resposta_correta]}\n")
        return False


def quiz():
    perguntas = [
        {
            "pergunta": "Qual é o resultado de 5 + 3 * 2?",
            "alternativas": ["16", "11", "10", "13"],
            # Indice da resposta correta (baseado em zero)
            "resposta_correta": 1
        },
        {
            "pergunta": "Qual é o resultado de (5 + 3) * 2?",
            "alternativas": ["16", "11", "10", "13"],
            "resposta_correta": 0
        },
        {
            "pergunta": "Qual é o resultado de 2 ** 3 ** 2?",
            "alternativas": ["64", "512", "256", "128"],
            "resposta_correta": 1
        },
        {
            "pergunta": "Qual é o resultado de 4 + 2 / 2",
            "alternativas": ["3", "4", "5", "6"],
            "resposta_correta": 2
        },
        {
            "pergunta": "Qual é o resultado de (4 + 2) / 2",
            "alternativas": ["3", "4", "5", "6"],
            "resposta_correta": 0
        },
        {
            "pergunta": "Qual é o resultado de 2 * 2 ** 3 // 2",
            "alternativas": ["32", "5", "8", "4"],
            "resposta_correta": 2
        },
    ]

    score = 0
    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["alternativas"], pergunta["resposta_correta"]):
            score += 1

    print(f"Você acertou {score} de {len(perguntas)} perguntas.")


if __name__ == "__main__":
    quiz()
2
