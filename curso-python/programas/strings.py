import string
from keyword import iskeyword

print('=' * 50)
print('1.0 - Codificação de caractares: Função ord')
print('-' * 50)

# 1.1 - (resolvido) Imprima o valor unicode dos seguintes caracteres: A, X e <
#print('Unicode de A: ', ord('A'))
#print('Unicode de X: ', ord('X'))
#print('Unicode de <: ', ord('<'))

# 1.2 - Imprima o valor unicode dos seguintes caracteres: B, *, @, ∑


# 1.3 - (resolvido) Imprima o valor unicode das letras minúsculas do nosso alfabeto (a até z)
#for caracter in string.ascii_lowercase:
#    print(f'Unicode de {caracter}: {ord(caracter)}')

# 1.4 - Imprima o valor unicode das letras maiúsculas do nosso alfabeto (A até Z)


# 1.5 - Imprima o valor unicode dos números de 0 a 9
# Dica, use a função range pra gerar a lista de números
# Sintaxe: range(start, stop, step)
# start: Opcional. Um número inteiro que especifica em qual posição iniciar. O padrão é 0
# stop:	Obrigatório. Um número inteiro especificando em qual posição parar (não incluído).
# step:	Opcional. Um número inteiro que especifica a incrementação. O padrão é 1

print('=' * 50)
print('2.0 - Decodificação de caractares: Função chr')
print('-' * 50)

# 2.1 - (resolvido) Descubra qual caractere possui o código 66
# print(f'Unicode 66 corresponde ao caractere: {chr(66)}')

# 2.2 - Imprima os caracteres com os seguintes códigos unicode: 78, 106, 3088

print('=' * 50)
print('3.0 - Definindo strings')
print('-' * 50)

# 3.1 - Imprima a string Imprima a string "Olá Mundo" usando aspas simples

# 3.2 - Imprima a string Imprima a string "Olá Mundo" usando aspas duplas

# 3.3 - Imprima a string Imprima a string "Olá Mundo" usando aspas triplas

# 3.4 - Imprima a string Imprima a string "Olá Mundo" usando aspas triplas duplas

# 3.5 - Imprima a string "My name's Richard" usando aspas duplas pra definição da string

# 3.6 - Imprima a string 'My name's Richard' usando aspas simples pra definição da string
# Dica: Use o caractere de escape \ para escapar a aspa simples

print('=' * 50)
print('4.0 - Índices de strings')
print('-' * 50)

# 4.1 - Imprima o primeiro caractere da string "Python"

# 4.2 - Imprima o primeiro caractere da string "Python" usando índices negativos

# 4.3 - Imprima o último caractere da string "Python"

# 4.4 - Imprima o último caractere da string "Python" usando índices negativos

print('=' * 50)
print('5.0 - Fatiamento de strings')
print('-' * 50)

# Vamos considerar a string 'Olá, Mundo!'
minha_string = 'Olá, Mundo!'

# 5.1 - (resolvido) Pegar os primeiros 3 caracteres (Saída: Olá)
#print(minha_string[:3])

# 5.2 - (resolvido) Pegar os últimos 3 caracteres (Saída: do!)
#print(minha_string[-3:])

# 5.3 - (resolvido) Pegar caracteres do índice 2 ao índice 5 (Saída: a, M)
#print(minha_string[2:6])

# 5.4 - (resolvido) Pegar todos os caracteres em posições ímpares (Saída: Oá ud!)
#print(minha_string[::2])

# Vamos considerar uma nova string: 'Python é divertido'
nova_string = 'Python é divertido'

# 5.5 - Formar a substring 'Python' a partir da nova string (Saída: Python)

# 5.6 - Formar a substring 'divertido' a partir da nova string (Saída: divertido)

print('=' * 50)
print('6.0 - Revertendo strings')
print('-' * 50)

# 6.1 - Reverter a string 'Python' (Saída: nohtyP)

print('=' * 50)
print('7.0 - Métodos em strings')
print('-' * 50)

# Para os próximos exercícios, considere a string ' Python é divertido '
minha_string = ' Python é divertido '

# 7.1 - Remova os espaços que aparecem na string ' Python é divertido '


# 7.2  - Informe o tamanho da string 'Python é divertido'


# 7.3 - Converta a string 'Python é divertido' para letras minusculas

# 7.4 - Converta a string 'Python é divertido' para letras maiúsculas

# 7.5 - Troque as letras maiúsculas da string 'Python é divertido' por letras minúsculas e vice-versa

# 7.6 - Coloque a primeira letra de cada palavra da string 'Python é divertido' em maiúscula

# 7.7 - Substitua a palavra 'divertido' por 'fantástico' na string 'Python é divertido'

# 7.8 - Retorne uma lista das palavras da string 'Python é divertido'

# 7.9 - Verifique a quantidade de ocorrências da letra 'o' na string 'Python é divertido'

# 7.10 - Verifique se a string 'Python é divertido' começa com a palavra 'Python'

# 7.11 - Verifique se a string 'Python é divertido' termina com a palavra 'divertido'

# 7.12 - Verifique se a string 'Python é divertido' começa com a palavra 'python'

# 7.13 - Verifique se a string 'Python é divertido' termina com a palavra 'fantástico'

# 7.14 - Verifique em que posição a palavra divertido aparece na string 'Python é divertido'

# 7.15 - Verifique em que posição a palavra 'fantástico' aparece na string 'Python é divertido'

# 7.16 - Verifique em que posição a palavra 'Python' aparece na string 'Python é divertido'

# 7.17 - Verifique se a string 'Python é divertido' é formada apenas por letras e números

# 7.18 - Verifique se a string 'Python é divertido' é formada apenas por letras

# 7.19 - Verifique se a string 'Pythonédivertido' é formada apenas por letras e números

# 7.20 - Verifique se a string 'Pythonédivertido' é formada apenas por letras

# 7.21 - Verifique se a string '12345' é formada apenas por números

# 7.22 - Verifique se a string '12345a' é formada apenas por números

# 7.23 - Verifique se a string 'nome' é um identificador válido

# 7.24 - Verifique se a string 'nome 2' é um identificador válido

# 7.25 - Verifique se a string '2nome' é um identificador válido

# 7.26 - Verifique se a string 'nome#' é um identificador válido

# 7.27 - Verifique se a string 'or' é uma palavra chave do Python

# 7.28 - Verifique se a string 'else' é uma palavra chave do Python

# 7.29 - Verifique se a string 'while' é uma palavra chave do Python

# 7.30 - Verifique se a string 'Gabriel\tFelippe' é imprimível

# 7.31 - Verifique se a string 'Gabriel Felippe' é imprimível

# 7.32 - Verifique se a string '' é um espaço

# 7.33 - Verifique se a string ' ' é um espaço

# 7.34 - Verifique se a string 'x' é um espaço

# 7.35 - Verifique se a string '\t\n' é um espaço

# 7.36 - Verifique se a string 'STRING' está em maiúsculas

# 7.37 - Verifique se a string 'String' está em maiúsculas

# 7.38 - Verifique se a string 'String' está em minúsculas

# 7.39 - Verifique se a string 'string' está em minúsculas

print('=' * 50)
print('Fim dos exercícios')
print('-' * 50)
