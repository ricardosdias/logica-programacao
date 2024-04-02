import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Constantes
NUM_MINAS = 10
GRID_SIZE = 10
CELULA_TAMANHO = 40
LARGURA, ALTURA = CELULA_TAMANHO * GRID_SIZE, CELULA_TAMANHO * GRID_SIZE + 60
FONT = pygame.font.SysFont('Arial', 25)
CORES = {
    'seguro': (170, 215, 81),
    'mina': (209, 47, 47),
    'padrao': (192, 192, 192),
    'texto': (255, 255, 255),
    'numeros': [
        (0, 0, 255),
        (0, 128, 0),
        (255, 0, 0),
        (0, 0, 128),
        (128, 0, 0),
        (0, 128, 128),
        (0, 0, 0),
        (128, 128, 128),
    ]
}

# Inicializa a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Campo Minado")

# Funções


def criar_campo():
    campo = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Colocar as minas
    minas_plantadas = 0
    while minas_plantadas < NUM_MINAS:
        x, y = random.randint(
            0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if campo[y][x] == 0:
            campo[y][x] = -1
            minas_plantadas += 1

            # Incrementar os números ao redor da mina
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE and campo[y + dy][x + dx] != -1:
                        campo[y + dy][x + dx] += 1
    return campo


def desenhar_celulas(tela, campo, revelado, pontuacao):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * CELULA_TAMANHO, y *
                               CELULA_TAMANHO, CELULA_TAMANHO, CELULA_TAMANHO)
            if revelado[y][x]:
                if campo[y][x] == -1:
                    pygame.draw.rect(tela, CORES['mina'], rect)
                else:
                    pygame.draw.rect(tela, CORES['seguro'], rect)
                    if campo[y][x] > 0:
                        text = FONT.render(
                            str(campo[y][x]), True, CORES['numeros'][campo[y][x] - 1])
                        tela.blit(text, text.get_rect(center=rect.center))
            else:
                pygame.draw.rect(tela, CORES['padrao'], rect)
            pygame.draw.rect(tela, (0, 0, 0), rect, 1)
    desenhar_placar(tela, pontuacao)


def desenhar_placar(tela, pontuacao):
    placar_rect = pygame.Rect(0, CELULA_TAMANHO * GRID_SIZE, LARGURA, 60)
    pygame.draw.rect(tela, (0, 0, 0), placar_rect)
    placar_texto = FONT.render(f'Pontuação: {pontuacao}', True, CORES['texto'])
    tela.blit(placar_texto, placar_texto.get_rect(
        center=(LARGURA // 2, ALTURA - 30)))


def revelar_celula(tela, campo, revelado, x, y, pontuacao):
    if not revelado[y][x]:
        revelado[y][x] = True
        if campo[y][x] == -1:
            mostrar_todas_minas(tela, campo, revelado)
            desenhar_celulas(tela, campo, revelado, pontuacao)
            pygame.display.flip()
            return True, pontuacao  # Jogo perdido, pontuação não muda
        elif campo[y][x] == 0:
            # Revela células adjacentes
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE:
                        _, pontuacao = revelar_celula(
                            tela, campo, revelado, x + dx, y + dy, pontuacao)
        else:
            pontuacao += 1  # Incrementa a pontuação para cada célula segura revelada
    return False, pontuacao


def mostrar_todas_minas(tela, campo, revelado):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if campo[y][x] == -1:
                revelado[y][x] = True


def clicou_na_mina(tela, pontuacao):
    # Atualiza a tela para mostrar a mina clicada
    # (você precisará adicionar a lógica para desenhar a mina clicada aqui)
    pygame.display.flip()

    # Pausa o jogo por 4000 milissegundos (4 segundos)
    pygame.time.delay(4000)

    # Depois do atraso, chama a função que pergunta se o jogador quer reiniciar ou sair
    return perguntar_reiniciar(tela, pontuacao)


def perguntar_reiniciar(tela, pontuacao):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Exibe a mensagem na tela
        tela.fill((0, 0, 0))
        mensagem_linha_1 = FONT.render(
            f'Você perdeu! Sua pontuação foi: {pontuacao}', True, CORES['texto'])
        mensagem_linha_2 = FONT.render(
            'Pressione R para jogar novamente', True, CORES['texto'])
        mensagem_linha_3 = FONT.render('ou Q para sair.', True, CORES['texto'])

        # Calcula o centro vertical para as mensagens
        centro_y = ALTURA // 2
        tela.blit(mensagem_linha_1, mensagem_linha_1.get_rect(
            center=(LARGURA // 2, centro_y - 30)))
        tela.blit(mensagem_linha_2, mensagem_linha_2.get_rect(
            center=(LARGURA // 2, centro_y)))
        tela.blit(mensagem_linha_3, mensagem_linha_3.get_rect(
            center=(LARGURA // 2, centro_y + 30)))
        pygame.display.flip()


# Jogo
campo = criar_campo()
revelado = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
pontuacao = 0
desenhar_celulas(tela, campo, revelado, pontuacao)
pygame.display.flip()

# Loop do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x, grid_y = x // CELULA_TAMANHO, y // CELULA_TAMANHO
            if grid_y < GRID_SIZE:
                perdido, pontuacao = revelar_celula(
                    tela, campo, revelado, grid_x, grid_y, pontuacao)
                desenhar_celulas(tela, campo, revelado, pontuacao)
                pygame.display.flip()
                if perdido:
                    if clicou_na_mina(tela, pontuacao):
                        campo = criar_campo()
                        revelado = [[False for _ in range(
                            GRID_SIZE)] for _ in range(GRID_SIZE)]
                        pontuacao = 0
                        desenhar_celulas(tela, campo, revelado, pontuacao)
                        pygame.display.flip()
                    else:
                        rodando = False

pygame.quit()
