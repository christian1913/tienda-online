import argparse
from bs4 import BeautifulSoup

def add_suffix_to_classes(html_file, suffix):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for tag in soup():
        if 'class' in tag.attrs:
            new_classes = [f'{c}-{suffix}' for c in tag['class']]
            tag['class'] = new_classes

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Añadir sufijo a las clases de un archivo HTML.')
    parser.add_argument('-s', '--string', help='Palabra que se añadirá como sufijo a todas las clases HTML.', required=True)
    parser.add_argument('-a', '--archivo', help='Archivo HTML que se modificará.', required=True)

    args = parser.parse_args()

    add_suffix_to_classes(args.archivo, args.string)
