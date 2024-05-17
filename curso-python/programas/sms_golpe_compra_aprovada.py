import csv
import os

# Cria a pasta SMS_GOLPE
pasta_sms = 'SMS_GOLPE'
os.makedirs(pasta_sms, exist_ok=True)

TEMPLATE_SMS = '''
Olá {nome}!
Sua compra no valor de R 2.570,58 com o CPF {cpf} foi aprovada.
Para verificar o prazo de entrega clique aqui (www.lojadohacker.com.br/{cpf})
'''

# Lê o arquivo dados_ficticios.csv
csv_file = 'dados_ficticios.csv'
arquivo_dados_ficticios = open(csv_file, mode='r', newline='')
reader = csv.reader(arquivo_dados_ficticios)
header = next(reader)
for row in reader:
    nome, endereco, telefone, aniversario, cpf = row
    sms = TEMPLATE_SMS.format(nome=nome, cpf=cpf)
    path = os.path.join(pasta_sms, telefone + '.txt')
    with open(path, mode='w') as file:
        file.write(sms)


