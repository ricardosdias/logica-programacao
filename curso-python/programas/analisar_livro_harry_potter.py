# https://github.com/bobdeng/owlreader/blob/master/ERead/assets/books/Harry%20Potter%20and%20The%20Half-Blood%20Prince.txt
nome_arquivo = "Harry Potter and The Half-Blood Prince.txt"
nome_arquivo_alterado = "Harry Potter and The Half-Blood Prince2.txt"
livro = open(nome_arquivo, "r", encoding="utf-8")
texto = livro.read()
livro.close()

# Contar caracteres
# numero_caracteres = ?
# print('Número de caracteres:', numero_caracteres)

# Contar palavras
# palavras = ?
# numero_palavras = ?
# print('Número de palavras:', numero_palavras)

# Contar frases
# frases = ?
# numero_frases = ?
# print('Número de frases:', numero_frases)

# Contar parágrafos
# paragrafos = ?
# numero_paragrafos = ?
# print('Número de parágrafos:', numero_paragrafos)

# Encontra a primeira posição da palavra "Harry"
# posicao = ?
# print('Posição da primeira ocorrência de "Harry":', posicao)

# Encontra a primeira posição da palavra "Herminone"
# posicao = ?
# print('Posição da primeira ocorrência de "Hermione":', posicao)

# Reverter a primeira linha do texto e mostrar na tela
# primeira_linha = ?
# primeira_linha_revertida = ?
# print('Primeira linha revertida:', primeira_linha_revertida)

# Alterar o nome do personagem principal para Seu Nome
# novo_texto = ?
# open(nome_arquivo_alterado, "w", encoding="utf-8").write(novo_texto)
