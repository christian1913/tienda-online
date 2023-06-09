import os
import sys
import subprocess

def apply_uncss(html_folder, css_folder):
    for dirpath, dirnames, filenames in os.walk(html_folder):
        for filename in filenames:
            if filename.endswith('.html') and filename not in ['index.html', 'base.html']:
                html_path = os.path.join(dirpath, filename)
                relative_dir = os.path.relpath(dirpath, html_folder)
                css_dir = os.path.join(css_folder, relative_dir)
                os.makedirs(css_dir, exist_ok=True)
                css_path = os.path.join(css_dir, filename.replace('.html', '.css'))
                cmd = f'uncss {html_path} > {css_path}'
                try:
                    subprocess.run(cmd, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error al procesar {html_path}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <html_folder> <css_folder>")
        sys.exit(1)

    html_folder = sys.argv[1]
    css_folder = sys.argv[2]

    apply_uncss(html_folder, css_folder)
