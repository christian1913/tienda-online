import argparse
import cssutils

def add_suffix_to_classes(css_file, suffix):
    css_parser = cssutils.CSSParser()

    cssutils.log.raiseExceptions = False

    with open(css_file, 'r', encoding='utf-8') as file:
        stylesheet = css_parser.parseString(file.read())

    for rule in stylesheet:
        if rule.type == rule.STYLE_RULE:
            classes = rule.selectorText.split(',')
            new_classes = []
            for c in classes:
                if '.' in c:
                    class_name, selector = c.split('.', 1)
                    new_classes.append(f'{class_name}.{selector}-{suffix}')
                else:
                    new_classes.append(c)

            rule.selectorText = ', '.join(new_classes)

    with open(css_file, 'w', encoding='utf-8') as file:
        file.write(stylesheet.cssText.decode("utf-8"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Añadir sufijo a las clases de un archivo CSS.')
    parser.add_argument('-s', '--string', help='Palabra que se añadirá como sufijo a todas las clases CSS.', required=True)
    parser.add_argument('-a', '--archivo', help='Archivo CSS que se modificará.', required=True)

    args = parser.parse_args()

    add_suffix_to_classes(args.archivo, args.string)

