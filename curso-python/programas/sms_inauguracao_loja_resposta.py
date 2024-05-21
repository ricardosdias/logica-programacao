'''
Criar um programa pra mandar um SMS pra todos os clientes
Convidando os mesmos pra inauguração da nova loja.

A lista de clientes está no arquivo clientes.csv
As mensagens de SMS deverão ser guardadas na pasta SMS_CONVITE

As colunas do arquivo clientes.csv são: Nome,Telefone,Aniversário,CPF,RG
Utilizar o RG para gerar o arquivo com a mensagem de inauguração.
'''

import csv
import os

# Cria a pasta SMS_CONVITE
pasta_sms = 'SMS_CONVITE'
os.makedirs(pasta_sms, exist_ok=True)

TEMPLATE_SMS = '''
Olá {nome}!
Gostaria de convidá-lo pra inauguração da nossa loja
que irá ocorrer 01/06/2024 no endereço Rua A, casa 02, Rio.
Teremos um coquetel!
'''

csv_file = 'clientes.csv'
arquivo_clientes = open(
    csv_file, mode='r', newline='', encoding='utf-8')
reader = csv.reader(arquivo_clientes)
header = next(reader)
for row in reader:
    nome, telefone, aniversario, cpf, rg = row
    sms = TEMPLATE_SMS.format(nome=nome)
    path = os.path.join(pasta_sms, rg + '.txt')
    with open(path, mode='w', encoding='utf-8') as file:
        file.write(sms)
