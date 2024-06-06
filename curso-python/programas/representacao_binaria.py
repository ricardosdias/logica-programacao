# ---------------------------------------------------
# Representação Binária
# ---------------------------------------------------

print('Exercício 1: Conversão de Decimal para Binário')
num = 13

# Use a função embutida bin() para converter num em binário
# Atribua o resultado a variável binario
# Coloque seu código AQUI


# Descomente o código abaixo para verificar a conversão
print(f'O número {num} em binário é {binario}')

print('\nExercício 2: Conversão de Binário para Decimal')
binario = '1101'

# Use a função embutida int() para converter binario em decimal
# Atribua o resultado a variável decimal
# Coloque seu código AQUI


# Descomente o código abaixo para verificar a conversão
print(f'O número binário {binario} em decimal é {decimal}')

print('\nExercício 3: Conversão de Decimal para Binário sem usar as funções embutidas')

# Escreva uma função que recebe um número decimal e retorna sua representação em binário


def converte_decimal_binario(decimal):
    # Inicializa a variável binario como uma string vazia
    binario = ''

    # Enquanto decimal for diferente de 0
    while decimal != 0:
        # Calcula o resto da divisão de decimal por 2
        # Coloque seu código AQUI

        # Adiciona o resto à esquerda da string binario
        # Coloque seu código AQUI

        # Atualiza o valor de decimal dividindo por 2 (divisão inteira)
        # Coloque seu código AQUI

        # Se binario ainda estiver vazio, significa que o número era 0

        pass

    if binario == '':
        binario = '0'

    return binario


print(f'O número {13} em binário é {converte_decimal_binario(13)}')
print(f'O número {26} em binário é {converte_decimal_binario(26)}')
print(f'O número {1} em binário é {converte_decimal_binario(1)}')


print('\nExercício 4: Conversão de Binário para Decimal sem usar as funções embutidas')

# Escreva uma função que recebe uma string com a representação binária e retorna o número decimal


def converte_binario_decimal(binario):
    # Inicializa a variável decimal como 0
    decimal = 0

    # Inicializa a variável potencia como 0
    potencia = 0

    # Itera sobre cada dígito do binario de trás para frente
    for digito in binario[::-1]:
        # Converte o dígito para inteiro
        # Coloque seu código AQUI

        # Adiciona o valor do dígito multiplicado por 2 elevado à potencia à variável decimal
        # Coloque seu código AQUI

        # Incrementa a potência
        # Coloque seu código AQUI

        pass

    return decimal


print(f'O binário {1101} em decimal é {converte_binario_decimal("1101")}')
print(f'O binário {1010} em decimal é {converte_binario_decimal("1010")}')
print(f'O binário {1111} em decimal é {converte_binario_decimal("1111")}')
