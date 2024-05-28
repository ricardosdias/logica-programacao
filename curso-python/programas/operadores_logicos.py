# ---------------------------------------------------
# Operadores Lógicos
# ---------------------------------------------------

print('Exercício 1: Login Simples')
''''
Escreva um programa que verifica se o nome de usuário e a senha fornecidos estão corretos
(nome de usuário: 'admin', senha: '1234').
'''
# Nome de usuário e senha corretos
usuario_correto = "admin"
senha_correta = "1234"

# Solicitar nome de usuário e senha do usuário
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verificar se ambos estão corretos
# Coloque abaixo a expressão que verifica se o login está correto
# Atribua o resultado da expressão a variável login_correto


# Descomente o código abaixo para verificar se o login está correto
# print("Login correto:", login_correto)
# print(f"Nome de usuário: {usuario_correto}, senha: {senha_correta}")


print('\nExercício 2: Número dentro de vários intervalos')
'''
Escreva um programa que verifica se um número está dentro de um dos seguintes intervalos: 0 a 10, 20 a 30, ou 40 a 50.
'''
# Solicitar um número do usuário
numero = int(input("Digite um número: "))

# Verificar se está em um dos intervalos

# Verifica se o número está no intervalo 0 a 10:
intervalo_1 = 0 <= numero <= 10

# Verifica se o número está no intervalo 20 a 30:
# Coloque abaixo a expressão que verifica se o número está no intervalo 20 a 30
# Atribua o resultado da expressão a variável intervalo_2


# Verifica se o número está no intervalo 40 a 50:
# Coloque abaixo a expressão que verifica se o número está no intervalo 40 a 50
# Atribua o resultado da expressão a variável intervalo_3


# Verifica se o número está dentro de algum dos intervalos
# Coloque abaixo a expressão que verifica se o número está dentro de algum intervalo
# Atribua o resultado da expressão a variável dentro_de_algum_intervalo


# Descomente o código abaixo para verificar se o número está dentro de algum intervalo
# print("O número está dentro de um dos intervalos:", dentro_de_algum_intervalo)
# print('Intervalos: 0 a 10, 20 a 30, ou 40 a 50')


print('\nExercício 3: Par ou Ímpar')
''''
Escreva um programa que verifica se um número é par ou ímpar.
'''
# Solicitar um número do usuário
numero = int(input("Digite um número: "))

# Verificar se é par
par = numero % 2 == 0

# Coloque abaixo a expressão que verifica se o número é ímpar (use o operador lógico not)
# Atribua o resultado da expressão a variável impar


# Descomente o código abaixo para verificar se o número é par ou ímpar
# print("Par:", par)
# print("Ímpar:", impar)
