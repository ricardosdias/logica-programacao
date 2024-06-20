# ---------------------------------------------------
# Listas
# ---------------------------------------------------

def print_cabecalho1_secao():
    print('\n')
    print('-' * 80)

def print_cabecalho2_secao():
    print('-' * 80)

print_cabecalho1_secao()
print('Seção 1: Criando listas!')
print_cabecalho2_secao()

print('\nExercício 1.1: '
    'Crie uma lista vazia e imprima a lista na tela.')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.2: '
    'Crie uma lista com 3 elementos inteiros e imprima-a na tela.')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.3: '
    'Crie uma lista com 3 elementos de tipos diferentes e imprima-a na tela.')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.4: '
    'Crie uma lista com 3 listas e imprima-a na tela:')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.5: '
    'Criei uma lista com os nomes dos seus colegas de turma e imprima-a na tela.')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 2: Acessando elementos individuais de uma lista!')
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(f'Lista: {a}')
print_cabecalho2_secao()

print('\nExercício 2.1: '
    'Acesse o primeiro elemento da lista e imprima-o na tela')
print('Resultado esperado: foo')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.2: '
    'Acesse o último elemento da lista e imprima-o na tela. '
    'Use o índice positivo.')
print('Resultado esperado: corge')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.3: '
    'Acesse o último elemento da lista e imprima-o na tela. '
    'Desta vez use o índice negativo.')
print('Resultado esperado: corge')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.4: '
    'Acesse o penúltimo elemento da lista e imprima-o na tela. '
    'Use o índice negativo.')
print('Resultado esperado: quux')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.5: '
    'Acesse o primeiro elemento da lista e imprima-o na tela. '
    'Use índice negativo.')
print('Resultado esperado: foo')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 3: Acessando partes de uma lista (fatiamento ou slicing)!')

print(f'Lista: {a}')
print_cabecalho2_secao()

print('\nExercício 3.1: '
    'Imprima os 3 primeiros elementos da lista, usando a técnica de fatiamento. '
    'Use índices positivos e não omita os índices no fatiamento.')
print('Resultado esperado: [\'foo\', \'bar\', \'baz\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.2: '
    'Imprima os 3 primeiros elementos da lista, usando a técnica de fatiamento. '
    'Use índices positivos, mas sem especificar o índice inicial.')
print('Resultado esperado: [\'foo\', \'bar\', \'baz\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.3: '
    'Imprima os 3 primeiros elementos da lista, usando a técnica de fatiamento. '
    'Use índices negativos e não omita os índices no fatiamento.')
print('Resultado esperado: [\'foo\', \'bar\', \'baz\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.4: '
    'Imprima os 3 primeiros elementos da lista, usando a técnica de fatiamento. '
    'Use índices negativos, mas sem especificar o índice inicial.')
print('Resultado esperado: [\'foo\', \'bar\', \'baz\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.5: '
    'Imprima os 3 últimos elementos da lista, usando a técnica de fatiamento. '
    'Use índices positivos e não omita os índices no fatiamento.')
print('Resultado esperado: [\'qux\', \'quux\', \'corge\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.6: '
    'Imprima os 3 últimos elementos da lista, usando a técnica de fatiamento. '
    'Use índices positivos, mas sem especificar o índice final.')
print('Resultado esperado: [\'qux\', \'quux\', \'corge\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.7: '
    'Imprima os 3 últimos elementos da lista, usando a técnica de fatiamento. '
    'Use índice negativo para o início da lista e índice positivo para o final.')
print('Resultado esperado: [\'qux\', \'quux\', \'corge\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.8: '
    'Imprima os 3 últimos elementos da lista, usando a técnica de fatiamento. '
    'Use índice negativo para o início da lista e desta vez omita o índice final.')
print('Resultado esperado: [\'qux\', \'quux\', \'corge\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.9: '
      'Imprima o anti penúltimo e o penúltimo elementos da lista, '
      'usando a técnica de fatiamento. '
      'Use indices negativos e não omita os índices no fatiamento.')
print('Resultado esperado: [\'qux\', \'quux\']')
# ESCREVA SEU CÓDIGO AQUI


print_cabecalho1_secao()
print('Seção 4: Usando o argumento de step no Slice!')
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Lista: {b}')
print_cabecalho2_secao()

print('\nExercício 4.1: '
    'Imprima os elementos da lista de 1 em 1, começando do primeiro elemento.')
print('Resultado esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.2: '
    'Imprima os elementos da lista de 2 em 2, começando do primeiro elemento.')
print('Resultado esperado: [1, 3, 5, 7, 9]')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.3: '
    'Imprima os elementos da lista de 2 em 2, começando do segundo elemento.')
print('Resultado esperado: [2, 4, 6, 8, 10]')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.4: '
    'Imprima os elementos da lista de 2 em 2, começando do último elemento.')
print('Resultado esperado: [10, 8, 6, 4, 2]')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.5: '
    'Imprima os elementos da lista de 1 em 1, começando do último elemento.')
print('Resultado esperado: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.6: '
      'Imprima a lista invertendo a ordem dos elementos.')
print('Resultado esperado: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 5: Copiando uma lista!')
frutas = ['maçã', 'banana', 'laranja', 'uva']
print(f'Lista: {frutas}')
print_cabecalho2_secao()

print('\nExercício 5.1: '
    'Copie a lista de frutas e imprima a cópia na tela. '
    'Guarde a cópia da lista em uma variável chamada frutas_copia. '
    'Use a técnica de fatiamento.')
print('Resultado esperado: [\'maçã\', \'banana\', \'laranja\', \'uva\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 5.2: '
    'Altere o primeiro elemento da lista de frutas para "melancia" e '
    'imprima a lista original e a cópia na tela.')
print('Resultado esperado: [\'melancia\', \'banana\', \'laranja\', \'uva\']')
print('Resultado esperado: [\'maçã\', \'banana\', \'laranja\', \'uva\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 5.3: '
    'Atribua a lista de frutas à variável frutas_copia2 e '
    'imprima frutas_copia2 na tela.')
print('Resultado esperado: [\'melancia\', \'banana\', \'laranja\', \'uva\']')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 5.4: '
    'Altere o primeiro elemento da lista de frutas para "morango" e '
    'imprima a lista original e a cópia na tela.')
print('Resultado esperado: [\'morango\', \'banana\', \'laranja\', \'uva\']')
print('Resultado esperado: [\'morango\', \'banana\', \'laranja\', \'uva\']')
# ESCREVA SEU CÓDIGO AQUI





