'''
Este programa lê um arquivo XML chamado atendimentos_hospital.xml
Percorre os elementos do arquivo e imprime as seguintes informações:
- Nível do elemento (0 pro elemento root, 1 pro primeiro filho, 2 pro segundo filho e assim por diante)
- Nome do elemento (ou tag)
- Atributos do elemento
- Texto do elemento
'''

import xml.etree.ElementTree as ET

ARQUIVO_XML = 'atendimentos_hospital.xml'

def print_elements(element, level=0):
    print(f'{"-" * level}Nível: {level}, Nome do Elemento: {element.tag}, Atributos: {element.attrib}, Texto: {element.text.strip() if element.text else ""}')
    for child in element:
        print_elements(child, level + 1)

tree = ET.parse(ARQUIVO_XML)
root = tree.getroot()

print_elements(root)