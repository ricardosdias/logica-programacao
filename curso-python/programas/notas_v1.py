import csv


def carregar_arquivo_notas(nome_arquivo):
    arquivo_notas = open(nome_arquivo, mode='r', newline='', encoding='utf-8')
    reader = csv.reader(arquivo_notas)
    header = next(reader)
    lista_notas = []
    for row in reader:
        disciplina, aluno, nota1, nota2, nota3, nota4 = row
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        nota4 = float(nota4)
        lista_notas.append([disciplina, aluno, nota1, nota2, nota3, nota4])
    return lista_notas


def imprimir_notas(lista):
    for registro in lista:
        print(registro)
    print()


def obter_primeiro_registro_da_lista(lista):
    # Escrever a função que retorna o primeiro registro da lista
    # Substitua o código abaixo pela sua função
    # return []
    return lista[0]



def obter_10_primeiros_registros(lista):
    # Escrever a função que retorna os 10 primeiros registro da lista
    # Substitua o código abaixo pela sua função
    # return []
    return lista[:10]


def calcular_media_notas(nota1, nota2, nota3, nota4):
    # Escrever a função que retorna a média das notas
    # Arredondar a média para uma casa decimal
    # Substitua o código abaixo pela sua função
    return round( (nota1 + nota2 + nota3 + nota4) / 4, 1)


def adicionar_media_na_lista_de_notas(lista_notas):
    # Escrever a função que percorre a lista de notas
    # Para cada registro da lista, chamar a função calcular_media_notas passando as 4 notas do registro
    # Adicionar a média na lista_notas como um novo campo
    # Formato da lista_notas: [['disciplina', 'aluno', nota1, nota2, nota3, nota4], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media], ...]
    # Substitua o código abaixo pela sua função

    lista_saida = []
    for linha in lista_notas:
        disciplina, aluno, nota1, nota2, nota3, nota4 = linha
        media = calcular_media_notas(nota1, nota2, nota3, nota4)
        saida = linha + [media,]
        lista_saida.append(saida)

    return lista_saida


def adicionar_status(lista_com_media):
    # Escrever a função que percorre a lista de notas com média
    # Adicionar um campo 'status' na lista de notas com média
    # Para isso deve ser verificado se a média é maior ou igual a 6
    # Se for maior ou igual a 6, o status é 'Aprovado'
    # Se for menor que 6, o status é 'Reprovado'
    # Formato da lista com média: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Substitua o código abaixo pela sua função
    lista_saida = []
    for registo in lista_com_media:
        disciplina, aluno, nota1, nota2, nota3, nota4, media = registo
        if media >= 6:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
        saida = registo + [status]
        lista_saida.append(saida)
    return lista_saida


def lista_somente_aprovados(lista_com_status):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com os registros cujo status é 'Aprovado'
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Substitua o código abaixo pela sua função
    lista_saida = []
    for registro in lista_com_status:
        disciplina, aluno, nota1, nota2, nota3, nota4, media, status = registro
        if status == 'Aprovado':
            lista_saida.append(registro)
    return lista_saida


def lista_somente_reprovados(lista_com_status):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com os registros cujo status é 'Reprovado'
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Substitua o código abaixo pela sua função
    lista_saida = []
    for registro in lista_com_status:
        disciplina, aluno, nota1, nota2, nota3, nota4, media, status = registro
        if status == 'Reprovado':
            lista_saida.append(registro)
    return lista_saida



def lista_notas_disciplina(lista_notas, disciplina):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com os registros da disciplina informada
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Substitua o código abaixo pela sua função
    lista_saida = []
    for registro in lista_notas:
        #materia, aluno, nota1, nota2, nota3, nota4, media, status = registro
        #materia = registro[0]
        if registro[0] == disciplina:
            lista_saida.append(registro)
    return lista_saida


def lista_notas_aluno(lista_notas, aluno):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com os registros do aluno informado
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Substitua o código abaixo pela sua função
    lista_aluno = []
    for registro in lista_notas:
        if registro[1] == aluno:
            lista_aluno.append(registro)
    return lista_aluno


def disciplinas_aprovado(lista_notas, aluno):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com as disciplinas em que o aluno informado foi aprovado
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: ['disciplina1', 'disciplina2', ...]
    # Substitua o código abaixo pela sua função
    return []


def disciplinas_reprovado(lista_notas, aluno):
    # Escrever a função que percorre a lista de notas com média e status
    # Criar uma nova lista somente com as disciplinas em que o aluno informado foi reprovado
    # Formato da lista com média e status: [['disciplina', 'aluno', nota1, nota2, nota3, nota4, media, 'status'], ...]
    # Formato da lista de saída: ['disciplina1', 'disciplina2', ...]
    # Substitua o código abaixo pela sua função
    return []


def main():

    lista_notas_turma = carregar_arquivo_notas('notas.csv')
    # Campos do arquivo notas.csv: disciplina,aluno,nota1,nota2,nota3,nota4

    # A função acima lê o arquivo e cria uma lista de listas
    # Para cada linha do arquivo notas.csv é criado uma lista com os campos da linha (disciplina, aluno, nota1, nota2, nota3, nota4)
    # Esta lista é adicionada a lista_notas_turma

    # lista_notas_turma é uma lista de listas
    # Formato: [['disciplina', 'aluno', nota1, nota2, nota3, nota4], ...]
    # Exemplo: [['Matemática', 'Francisco', 10.0, 9.0, 8.0, 7.0], ...]

    print('Primeiro registro:')
    print(obter_primeiro_registro_da_lista(lista_notas_turma))
    print()

    # exit()
    print('10 primeiros registros:')
    imprimir_notas(obter_10_primeiros_registros(lista_notas_turma))

    # exit()
    print('Nova lista com média:')
    nova_lista_media = adicionar_media_na_lista_de_notas(lista_notas_turma)
    imprimir_notas(obter_10_primeiros_registros(nova_lista_media))

    #exit()
    print('Nova lista com status:')
    nova_lista_status = adicionar_status(nova_lista_media)
    imprimir_notas(obter_10_primeiros_registros(nova_lista_status))

    #exit()
    print('Lista somente com aprovados:')
    nova_somente_aprovados = lista_somente_aprovados(nova_lista_status)
    imprimir_notas(obter_10_primeiros_registros(nova_somente_aprovados))

    #exit()
    print('Nova somente reprovados:')
    nova_somente_reprovados = lista_somente_reprovados(nova_lista_status)
    imprimir_notas(obter_10_primeiros_registros(nova_somente_reprovados))

    # exit()
    print('Notas da disciplina Ciências:')
    notas_disciplina = lista_notas_disciplina(nova_lista_status, 'Ciências')
    imprimir_notas(obter_10_primeiros_registros(notas_disciplina))

    # exit()
    # Substitua 'Fred' pelo seu nome
    meu_nome = 'Fred'
    print(f'Notas do aluno {meu_nome}:')
    notas_aluno = lista_notas_aluno(nova_lista_status, meu_nome)
    imprimir_notas(notas_aluno)

    exit()
    print(f'Disciplinas em que {meu_nome} foi aprovado:')
    disciplinas = disciplinas_aprovado(nova_lista_status, meu_nome)
    imprimir_notas(disciplinas)

    exit()
    print(f'Disciplinas em que {meu_nome} foi reprovado:')
    disciplinas = disciplinas_reprovado(nova_lista_status, meu_nome)
    imprimir_notas(disciplinas)


if __name__ == "__main__":
    main()
