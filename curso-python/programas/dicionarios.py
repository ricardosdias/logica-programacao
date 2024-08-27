# ---------------------------------------------------
# Dicionários
# ---------------------------------------------------

print('\nExercício 01:\n'
      'Crie um dicionário vazio usando o construtor dict e imprima o resultado\n'
      'Saída esperada:\n{}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 02:\n'
      'Crie um dicionário vazio usando chaves {} e imprima o resultado\n'
      'Saída esperada:\n{}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 03:\n'
      'Crie um dicionário com as seguintes chaves: nome e idade.\n'
      'Use o construtor dict e imprima o resultado\n'
      'Saída esperada:\n{\'nome\': \'Frodo\', \'idade\': 33}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 04:\n'
      'Crie um dicionário com as seguintes chaves: nome, idade e profissão.\n'
      'Use chaves {} e imprima o resultado\n'
      'Saída esperada:\n{\'nome\': \'Frodo\', \'idade\': 33, \'profissão\': \'Hobbit\'}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

meu_dicionario = {
    "nome": "Fred",
    "idade": 9,
    "profissão": "Mestre cuca",
    "altura": 1.80
}
print('\nExercício 05:\n'
      'No dicionário "meu_dicionario" definido acima, acesse o valor associado à chave "profissão"\n'
      'Use colchetes [] para acessar o valor e imprima o resultado\n'
      'Saída esperada:\nMestre cuca')

print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''


print('\nExercício 06:\n'
      'No dicionário "meu_dicionario" definido acima, acesse o valor associado à chave "idade"\n'
      'Use o método .get() para acessar o valor e imprima o resultado\n'
      'Saída esperada:\n9')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''


print('\nExercício 07:\n'
      'Imprima todas as chaves do dicionário "meu_dicionario" definido acima\n'
      'Use um laço for e imprima o resultado\n'
      'Não use o método .keys()\n'
      'Saída esperada:\nnome\nidade\nprofissão\naltura')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 08:\n'
      'Imprima todas as chaves do dicionário "meu_dicionario" definido acima\n'
      'Use um laço for com o método .keys() e imprima o resultado\n'
      'Saída esperada:\nnome\nidade\nprofissão\naltura')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 09:\n'
      'Imprima todos os valores do dicionário "meu_dicionario" definido acima\n'
      'Use um laço for com o método .values() e imprima o resultado\n'
      'Saída esperada:\nFred\n9\nMestre cuca\n1.8')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 10:\n'
      'Imprima todos os valores do dicionário "meu_dicionario" definido acima\n'
      'Use um laço for e imprima o resultado\n'
      'Não use o método .values()\n'
      'Saída esperada:\nFred\n9\nMestre cuca\n1.8')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 11:\n'
      'Imprima todas as chaves e valores do dicionário "meu_dicionario" definido acima\n'
      'Use um laço for e imprima o resultado\n'
      'Use f-string para formatar a saída\n'
      'Saída esperada:\nnome: Fred\nidade: 9\nprofissão: Mestre cuca\naltura: 1.8')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 12:\n'
      'Verifique se as chaves "nome" e "raça" estão presentes no dicionário "meu_dicionario" definido acima\n'
      'Imprima uma mensagem informando se a chave existe ou não\n'
      'Saída esperada:\nA chave \'nome\' existe no dicionário\nA chave \'raça\' não existe no dicionário')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 13:\n'
      'Verifique se os valores "Fred" e "Natasha" estão presentes no dicionário "meu_dicionario" definido acima\n'
      'Imprima uma mensagem informando se o valor existe ou não\n'
      'Saída esperada:\nO valor \'Fred\' existe no dicionário\nO valor \'Natasha\' não existe no dicionário')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 14:\n'
      'Crie um dicionário com os seguintes chaves: gerente, supervisor e analista1 e analista2\n'
      'Cada chave deve conter um dicionário com as chaves nome e idade\n'
      'Imprima o dicionário criado\n'
      'Saída esperada:\n'
      '{\'gerente\': {\'nome\': \'Frodo\', \'idade\': 33}, \'supervisor\': {\'nome\': \'Sam\', \'idade\': 30}, \'analista1\': {\'nome\': \'Merry\', \'idade\': 25}, \'analista2\': {\'nome\': \'Pippin\', \'idade\': 22}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''


print('\nExercício 15:\n'
      'Quantos itens tem o dicionário criado no exercício anterior?\n'
      'Quantos itens tem o sub-dicionário associado à chave "gerente"?\n'
      'Use a função len() para verificar\n'
      'Saída esperada:\n'
      '4\n'
      '2')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 16:\n'
      'Imprima o sub-dicionário associado à chave "supervisor" do dicionário criado no exercício 14\n'
      'Saída esperada:\n'
      '{\'nome\': \'Sam\', \'idade\': 30}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

alunos = {
    "aluno1": {
        "nome": "Frodo",
        "idade": 33
    },
    "aluno2": {
        "nome": "Sam",
        "idade": 30
    },
    "aluno3": {
        "nome": "Merry",
        "idade": 25
    },
    "aluno4": {
        "nome": "Pippin",
        "idade": 22
    }
}

print('\nExercício 17:\n'
      'Altere a idade do aluno1 para 35\n'
      'Imprima o dicionário alunos\n'
      'Saída esperada:\n'
      '{\'aluno1\': {\'nome\': \'Frodo\', \'idade\': 35}, \'aluno2\': {\'nome\': \'Sam\', \'idade\': 30}, \'aluno3\': {\'nome\': \'Merry\', \'idade\': 25}, \'aluno4\': {\'nome\': \'Pippin\', \'idade\': 22}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 18:\n'
      'Adicione um novo aluno ao dicionário alunos\n'
      'O novo aluno deve ter as seguintes informações: nome: Gandalf, idade: 100\n'
      'Imprima o dicionário alunos\n'
      'Saída esperada:\n'
      '{\'aluno1\': {\'nome\': \'Frodo\', \'idade\': 35}, \'aluno2\': {\'nome\': \'Sam\', \'idade\': 30}, \'aluno3\': {\'nome\': \'Merry\', \'idade\': 25}, \'aluno4\': {\'nome\': \'Pippin\', \'idade\': 22}, \'aluno5\': {\'nome\': \'Gandalf\', \'idade\': 100}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 19:\n'
      'Adicione o curso "Python" ao aluno1\n'
      'Imprima o dicionário alunos\n'
      'Saída esperada:\n'
      '{\'aluno1\': {\'nome\': \'Frodo\', \'idade\': 35, \'curso\': \'Python\'}, \'aluno2\': {\'nome\': \'Sam\', \'idade\': 30}, \'aluno3\': {\'nome\': \'Merry\', \'idade\': 25}, \'aluno4\': {\'nome\': \'Pippin\', \'idade\': 22}, \'aluno5\': {\'nome\': \'Gandalf\', \'idade\': 100}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 20:\n'
      'Crie um dicionário com as seguintes chaves: nome, idade\n'
      'Use o método update para adicionar as chaves cidade e estado ao dicionário\n'
      'Imprima o dicionário criado\n'
      'Saída esperada:\n'
      '{\'nome\': \'Frodo\', \'idade\': 35, \'cidade\': \'Rio de Janeiro\', \'estado\': \'RJ\'}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 21:\n'
      'Crie um dicionário chamado aluno com as seguintes chaves: nome_aluno, idade\n'
      'Crie um segundo dicionário chamado curso com as seguintes chaves: nome_curso, carga_horaria\n'
      'Use o método update para adicionar as chaves do dicionário curso ao dicionário aluno\n'
      'Imprima o dicionário aluno\n'
      'Saída esperada:\n'
      '{\'nome_aluno\': \'Frodo\', \'idade\': 35, \'nome_curso\': \'Python\', \'carga_horaria\': 40}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 22:\n'
      'Crie um dicionário com as seguintes chaves: nome, idade, cidade\n'
      'Use o método update para atualizar a chave cidade do dicionário criado\n'
      'Imprima o dicionário criado\n'
      'Saída esperada:\n'
      '{\'nome\': \'Frodo\', \'idade\': 35, \'cidade\': \'Rio de Janeiro\'}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''


print('\nExercício 23:\n'
      'Remova o aluno1 do dicionário alunos\n'
      'Use o método .pop() e imprima o dicionário alunos\n'
      'Saída esperada:\n'
      '{\'aluno2\': {\'nome\': \'Sam\', \'idade\': 30}, \'aluno3\': {\'nome\': \'Merry\', \'idade\': 25}, \'aluno4\': {\'nome\': \'Pippin\', \'idade\': 22}, \'aluno5\': {\'nome\': \'Gandalf\', \'idade\': 100}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 24:\n'
      'Remova a chave idade do aluno2\n'
      'Use o método del e imprima o dicionário alunos\n'
      'Imprima o dicionário alunos\n'
      'Saída esperada:\n'
      '{\'aluno2\': {\'nome\': \'Sam\'}, \'aluno3\': {\'nome\': \'Merry\', \'idade\': 25}, \'aluno4\': {\'nome\': \'Pippin\', \'idade\': 22}, \'aluno5\': {\'nome\': \'Gandalf\', \'idade\': 100}}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

print('\nExercício 25:\n'
      'Crie um dicionário que represente um produto de uma loja (nome, preço, quantidade, categoria)\n'
      'Imprima o dicionário criado\n'
      'Saída esperada:\n'
      '{\'nome\': \'Notebook\', \'preço\': 2500.00, \'quantidade\': 10, \'categoria\': \'Informática\'}')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''

notas = {
    'prova1': 8.5,
    'prova2': 7.5,
    'prova3': 9.0,
    'prova4': 6.0
}
print('\nExercício 26:\n'
      'Calcule a média das notas do dicionário notas definido acima\n'
      'Imprima o resultado\n'
      'Saída esperada:\n7.75')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI''
# media = sum(notas.values()) / len(notas)

cidades = {
    'Rio de Janeiro': {'população': 6.32, 'área': 1200, 'estado': 'RJ'},
    'São Paulo': {'população': 12.25, 'área': 1500, 'estado': 'SP'},
    'Belo Horizonte': {'população': 2.5, 'área': 600, 'estado': 'MG'},
    'Curitiba': {'população': 1.9, 'área': 400, 'estado': 'PR'},
    'Porto Alegre': {'população': 1.5, 'área': 500, 'estado': 'RS'},
    'Recife': {'população': 1.6, 'área': 300, 'estado': 'PE'},
    'Salvador': {'população': 2.9, 'área': 500, 'estado': 'BA'},
    'Fortaleza': {'população': 2.6, 'área': 600, 'estado': 'CE'},
    'Manaus': {'população': 2.2, 'área': 1000, 'estado': 'AM'},
    'Belém': {'população': 1.5, 'área': 500, 'estado': 'PA'},
    'Goiânia': {'população': 1.5, 'área': 300, 'estado': 'GO'},
    'Brasília': {'população': 3.0, 'área': 600, 'estado': 'DF'},
    'Florianópolis': {'população': 0.5, 'área': 300, 'estado': 'SC'},
    'Vitória': {'população': 0.5, 'área': 200, 'estado': 'ES'},
    'Natal': {'população': 0.9, 'área': 200, 'estado': 'RN'},
}

print('\nExercício 27:\n'
      'Imprima a cidade com a maior população do dicionário cidades definido acima\n'
      'Saída esperada:\nSão Paulo')
print('Resultado obtido:')
# ESCREVA SEU CÓDIGO AQUI
