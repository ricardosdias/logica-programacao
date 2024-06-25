# ---------------------------------------------------
# Listas
# ---------------------------------------------------

def print_cabecalho1_secao():
    print('\n')
    print('-' * 80)

def print_cabecalho2_secao():
    print('-' * 80)

print_cabecalho1_secao()
print('Seção 1: Percorrendo uma lista com a instrução for!')
cursos = ['Enfermagem', 'Administração', 'Engenharia', 'Direito', 'Medicina']
print(f'Lista: {cursos}')
print_cabecalho2_secao()

print('\nExercício 1.1: '
    'Use a instrução for para percorrer a lista de cursos e imprima cada elemento na tela.')
print('Resultado esperado: Enfermagem, Administração, Engenharia, Direito, Medicina')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.2: '
      'Use a instrução for para percorrer a lista de cursos e imprima cada elemento na tela, '
      'Desta vez, use o índice para acessar cada elemento da lista.')
print('Resultado esperado: Enfermagem, Administração, Engenharia, Direito, Medicina')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 2: Modificando listas!')
frutas = ['Maçã', 'Banana', 'Cereja']
print(f'Lista: {frutas}')
print_cabecalho2_secao()

print('\nExercício 2.1: '
    'Altere a lista de frutas, troque o elemento Banana por Morango e imprima a lista na tela.')
print('Resultado esperado: Maçã, Morango, Cereja')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.2: '
    'Adicione Laranja na lista de frutas e imprima a lista na tela.')
print('Resultado esperado: Maçã, Morango, Cereja, Laranja')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.3: '
    'Remova Cereja da lista de frutas e imprima a lista na tela.')
print('Resultado esperado: Maçã, Morango, Laranja')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 3: Outras maneiras de adicionar elementos em listas!')
alunos = ['João', 'Carlos', 'Mariana', 'Fernanda']
print(f'Lista: {alunos}')
print_cabecalho2_secao()

print('\nExercício 3.1: '
    'Adicione o aluno Pedro na lista de alunos e imprima a lista na tela.')
print('Resultado esperado: João, Carlos, Mariana, Fernanda, Pedro')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.2: '
    'Adicione os alunos Maria, José, Julia e Rafael na lista de alunos e imprima a lista na tela.')
print('Resultado esperado: João, Carlos, Mariana, Fernanda, Pedro, Maria, José, Julia, Rafael')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.3: '
    'Adicione o aluno Ana na posição 2 da lista de alunos e imprima a lista na tela.')
print('Resultado esperado: João, Ana, Carlos, Mariana, Fernanda, Pedro, Maria, José, Julia, Rafael')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 4: Removendo elementos de uma lista!')
bairros = ['Centro', 'Jardim', 'Vila', 'Bela Vista', 'São Francisco', 'Alto']
print(f'Lista: {bairros}')
print_cabecalho2_secao()

print('\nExercício 4.1: '
    'Remova o bairro Centro da lista de bairros e imprima a lista na tela. '
    'Use o método remove() para remover o elemento Centro.')
print('Resultado esperado: Jardim, Vila, Bela Vista, São Francisco', 'Alto')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.2: '
    'Remova o bairro Alto da lista de bairros e imprima a lista na tela. '
    'Use o método pop() para remover o elemento Alto.')
print('Resultado esperado: Jardim, Vila, Bela Vista, São Francisco')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 4.3: '
    'Remova o bairro Vila da lista de bairros e imprima a lista na tela. '
    'Use o método del para remover o elemento Vila.')
print('Resultado esperado: Jardim, Bela Vista, São Francisco')
# ESCREVA SEU CÓDIGO AQUI