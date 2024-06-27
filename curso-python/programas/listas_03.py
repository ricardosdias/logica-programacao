# ---------------------------------------------------
# Listas
# ---------------------------------------------------

def print_cabecalho1_secao():
    print('\n')
    print('-' * 80)

def print_cabecalho2_secao():
    print('-' * 80)

print_cabecalho1_secao()
print('Seção 1: Concatenando listas!')
print_cabecalho2_secao()

print('\nExercício 1.1: '
    'Crie uma lista com nomes de pessoas e outra lista com profissões.\n'
    'Concatene as duas listas e imprima o resultado na tela.\n'
    'Também imprima as listas de pessoas e profissões separadamente.')
print('\nExemplo de Resultado esperado: \n'
      "Lista de Pessoas: ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']\n"
      "Lista de Profissões: ['Enfermeiro', 'Engenheiro', 'Médico', 'Advogado', 'Professor']\n"
      "Lista Concatenada: ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Enfermeiro', 'Engenheiro', 'Médico', 'Advogado', 'Professor']")
print('\nResultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 1.2: '
      'Crie uma lista com números de 1 a 5 e outra lista com números de 6 a 10.\n'
      'Concatene as duas listas e imprima o resultado na tela.\n'
      'Também imprima as listas de números separadamente.')
print('\nExemplo de Resultado esperado: \n'
        "Lista de Números 1: [1, 2, 3, 4, 5]\n"
        "Lista de Números 2: [6, 7, 8, 9, 10]\n"
        "Lista Concatenada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print('\nResultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 2: Repetindo elementos de uma lista!')
print_cabecalho2_secao()

print('\nExercício 2.1: '
    'Crie uma lista com nomes de frutas e repita os elementos da lista 3 vezes.\n'
    'Imprima a lista original e a lista repetida na tela.')
print('\nExemplo de Resultado esperado: \n'
        "Lista de Frutas: ['Maçã', 'Banana', 'Cereja']\n"
        "Lista Repetida: ['Maçã', 'Banana', 'Cereja', 'Maçã', 'Banana', 'Cereja', 'Maçã', 'Banana', 'Cereja']")
print('\nResultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 2.2: '
    'Crie uma lista com números de 1 a 3 e repita os elementos da lista 4 vezes.\n'
    'Imprima a lista original e a lista repetida na tela.')
print('\nExemplo de Resultado esperado: \n'
        "Lista de Números: [1, 2, 3]\n"
        "Lista Repetida: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]")
print('\nResultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print_cabecalho1_secao()
print('Seção 3: Ordenando elementos de uma lista!')
mumeros = [3, 1, 2, -10, 50, 13, 7, 8, 9, 0, 4, 5, 6]
nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']
print(f'Lista de números para os exercícios 3.1 e 3.4: {mumeros}')
print(f'Lista de nomes para os exercícios 3.2 e 3.3: {nomes}')
print_cabecalho2_secao()


print('\nExercício 3.1: '
    'Ordene a lista de números em ordem crescente e imprima o resultado na tela.\n'
    'Use o método list.sort().')
print('Resultado esperado: [-10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 50]')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI


print('\nExercício 3.2: '
    'Ordene a lista de nomes em ordem alfabética e imprima o resultado na tela.\n'
    'Use o método sorted.')
print("Resultado esperado: ['Ana', 'Carlos', 'João', 'Maria', 'Pedro']")
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.3: '
    'Ordene a lista de nomes em ordem alfabética inversa e imprima o resultado na tela.\n'
    'Use o método sorted().')
print("Resultado esperado: ['Pedro', 'Maria', 'João', 'Carlos', 'Ana']")
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI

print('\nExercício 3.4: '
    'Ordene a lista de números em ordem decrescente e imprima o resultado na tela.\n'
    'Use o método list.sort().')
print('Resultado esperado: [50, 13, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -10]')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI
