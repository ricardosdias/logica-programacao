import xml.etree.ElementTree as ET

ARQUIVO_XML = 'atendimentos_hospital.xml'

def print_elements(element, level=0):
    print(f'{"-" * level}Nível: {level}, Nome do Elemento: {element.tag}, Atributos: {element.attrib}, Texto: {element.text.strip() if element.text else ""}')
    for child in element:
        print_elements(child, level + 1)

tree = ET.parse(ARQUIVO_XML)
root = tree.getroot()

print_elements(root)