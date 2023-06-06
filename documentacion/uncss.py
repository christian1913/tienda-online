import subprocess
import os

def generate_optimized_css(html_path, css_path, output_path):
    # Verifica que los archivos existen
    if not os.path.isfile(html_path):
        raise ValueError(f"No se encuentra el archivo HTML: {html_path}")
    if not os.path.isfile(css_path):
        raise ValueError(f"No se encuentra el archivo CSS: {css_path}")

    # Genera el comando
    command = f"uncss -H {html_path} {css_path} > {output_path}"

    # Ejecuta el comando
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()

# Usa la función
html_path = "C:\\Users\\User\\OneDrive\\Documentos\\GitHub\\tienda-online\\tienda-online\\templates\\frontend\\navbar.html"
css_path = "C:\\Users\\User\\OneDrive\\Documentos\\GitHub\\tienda-online\\tienda-online\\templates\\static\\css\\navbar.css"
output_path = "C:\\Users\\User\\OneDrive\\Documentos\\GitHub\\tienda-online\\tienda-online\\templates\\static\\css\\navbar2.css"
generate_optimized_css(html_path, css_path, output_path)
