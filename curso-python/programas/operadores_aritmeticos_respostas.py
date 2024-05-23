# ---------------------------------------------------
# Operadores Aritméticos
# ---------------------------------------------------

# ---------------------------------------------------
# 1.0 Adição (+)
# ---------------------------------------------------
print('1.1 - Declare duas variáveis "a" e "b" e atribua valores inteiros a elas.')
print('Em seguida imprima a soma das duas variáveis:')
a = 10
b = 20
print(a + b)

print('1.2 - Declare duas variáveis "c" e "d" e atribua valores float a elas.')
print('Em seguida imprima a soma das duas variáveis:')
c = 10.5
d = 20.5
print(c + d)

# ---------------------------------------------------
# 2.0 Subtração (-)
# ---------------------------------------------------
print('2.1 - Declare duas variáveis "e" e "f" e atribua valores inteiros a elas.')
print('Em seguida imprima a subtração das duas variáveis:')
e = 100
f = 50
print(e - f)

print('2.2 - Declare duas variáveis "g" e "h" e atribua valores float a elas.')
print('Em seguida imprima a subtração das duas variáveis:')
g = 100.5
h = 50.5
print(g - h)

# ---------------------------------------------------
# 3.0 Multiplicação (*)
# ---------------------------------------------------
print('3.1 - Declare duas variáveis "i" e "j" e atribua valores numéricos a elas (pode ser inteiros ou float).')
print('Em seguida imprima a multiplicação das duas variáveis:')
i = 10
j = 20.5
print(i * j)

# ---------------------------------------------------
# 4.0 Divisão (/)
# ---------------------------------------------------
print('4.1 - Declare duas variáveis "k" e "l" e atribua valores numéricos a elas (pode ser inteiros ou float).')
print('Em seguida imprima a divisão das duas variáveis:')
k = 100
l = 20
print(k / l)

# ---------------------------------------------------
# 5.0 Divisão Inteira (//)
# ---------------------------------------------------
print('5.1 - Declare duas variáveis "m" e "n" e atribua valores inteiros a elas.')
print('Em seguida imprima a divisão inteira das duas variáveis:')
m = 100
n = 20
print(m // n)

# ---------------------------------------------------
# 6.0 Módulo (%)
# ---------------------------------------------------
print('6.1 - Declare duas variáveis "o" e "p" e atribua valores inteiros a elas.')
print('Em seguida imprima o módulo das duas variáveis:')
o = 100
p = 20
print(o % p)

# ---------------------------------------------------
# 7.0 Exponenciação (**)
# ---------------------------------------------------
print('7.1 - Declare duas variáveis "q" e "r" e atribua valores inteiros a elas')
print('Em seguida imprima a exponenciação das duas variáveis')
q = 10
r = 3
print(q ** r)

# ---------------------------------------------------
# 8.0 - Exemplos Práticos
# ---------------------------------------------------

# Não esqueça de imprimir o resultado das questões abaixo

print("8.1 - Calcule a área de um retângulo com base 10 e altura 20:")
# Dica: Área = base * altura
base = 10
altura = 20
area = base * altura
print(area)

print("8.2 - Calcule a área de um círculo com raio 5:")
# Dica: Área = π * raio²
# Dica: π = 3.14
raio = 5
area = 3.14 * (raio ** 2)
print(area)

print("8.3 - Calcule a área de um triângulo com base 10 e altura 20")
# Dica: Área = (base * altura) / 2
base = 10
altura = 20
area = (base * altura) / 2
print(area)

print("8.4 - Converta a temperatura de 37 graus Celsius para Fahrenheit")
# Dica: Fórmula: fahrenheit = (celsius * 9/5) + 32
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

print("8.5 - Converta um tempo dado em minutos para horas e minutos")
# Exemplo: 150 minutos = 2 horas e 30 minutos
tempo = 150
horas = tempo // 60
minutos = tempo % 60
print(f"{horas} horas e {minutos} minutos")
