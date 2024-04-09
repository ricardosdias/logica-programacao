'''
Este programa lê o arquivo XML chamado atendimentos_hospital.xml
E gera um arquivo XML chamado atendimentos_hospital_atualizado.xml com as seguintes modificações:
1. Formata o CRM do médico, para que tenha 10 caracteres, completando com zeros a esquerda.
2. Atualiza o preço de todos os medicamentos em 15%.
'''

import xml.etree.ElementTree as ET

# Função para formatar CRM do médico
ARQUIVO_XML_ENTRADA = 'atendimentos_hospital.xml'
ARQUIVO_XML_SAIDA = 'atendimentos_hospital_atualizado.xml'

def format_crm(crm):
    return str(crm).zfill(10)

# Carrega o arquivo XML
tree = ET.parse(ARQUIVO_XML_ENTRADA)
root = tree.getroot()

# Percorre os atendimentos
for atendimento in root.findall('atendimento'):
    # Formata o CRM do médico
    crm_medico = atendimento.find('CRM_medico')
    crm_medico.text = format_crm(crm_medico.text)

    # Percorre os medicamentos
    for medicamento in atendimento.find('medicamentos'):
        # Aumenta o preço do medicamento em 15%
        preco = medicamento.find('preco')
        preco.text = str(round(float(preco.text) * 1.15, 2))

# Salva as alterações em um novo arquivo
tree.write(ARQUIVO_XML_SAIDA)