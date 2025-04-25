import os
import subprocess
import shutil
import re

def run_sphinx_build():
    print("Running sphinx-build...")
    os.environ['SPHINX_BUILDER'] = 'latex'
    result = subprocess.run(['sphinx-build', '--jobs', 'auto', '-b', 'latex', '.', '_build/en'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running sphinx-build: {result.stderr}")
        return False
    print("Sphinx build complete.")
    return True

def remove_svg_from_tex(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    with open(tex_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(tex_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if not (r'\sphinxincludegraphics' in line and '.svg' in line):
                file.write(line)

    print("SVG image references removed.")
    return True

def parse_tabulary_table(tex_content):
    table_pattern = re.compile(
        r'\\begin\{tabulary\}\{.*?\}(?:\[.*?\])?\{.*?\}(.*?)\\end\{tabulary\}',
        re.DOTALL
    )
    tables = table_pattern.findall(tex_content)
    parsed_tables = []

    for table in tables:
        rows = []
        for line in table.splitlines():
            line = line.strip()
            if line.endswith(r'\\'):
                cells = [cell.strip() for cell in line[:-2].split('&')]
                rows.append(cells)
        parsed_tables.append((table, rows))

    return parsed_tables

def encode_longtable(rows, col_spec='ll'):
    # Start the longtable environment with the correct column specification
    header = "\\begin{longtable}{" + col_spec + "}"

    # Build the table rows without sphinx-specific commands
    body = "\n".join(
        " & ".join(row) + r"\\"
        for row in rows
    )

    # End the longtable environment
    footer = "\\end{longtable}"

    return "\n".join([header, body, footer])

def convert_tabulary_to_longtable(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    with open(tex_file, 'r', encoding='utf-8') as file:
        tex_content = file.read()

    table_pattern = re.compile(
        r'\\begin\{tabulary\}\{.*?\}\[.*?\]\{(.*?)\}(.*?)\\end\{tabulary\}',
        re.DOTALL
    )

    def map_column_spec(tab_spec):
        # Paper dimensions and margins (in inches)
        page_width = 8.5  # letter size width
        margin_left_right = 1  # 1 inch margin on left and right
        usable_width = page_width - 2 * margin_left_right  # 6.5 inches usable width

        # Count the number of 'X' columns (assuming 'T' is replaced by 'X')
        num_columns = len([col for col in tab_spec if col == 'T'])

        # Calculate the column width by dividing the usable width by the number of columns
        if num_columns > 0:
            column_width = usable_width / num_columns  # in inches
            column_width = f"{column_width:.2f}in"  # format the width to two decimal places (in inches)
        else:
            column_width = '1in'  # default width for non-X columns (you can adjust this)

        # Construct the column specification with p{calculated_width} for each 'T'
        return '|' + '|'.join(f'p{{{column_width}}}' if col == 'T' else col for col in tab_spec) + '|'

    def clean_sphinx_commands(text):
        # Remove any Sphinx-specific LaTeX commands from the table content
        cleaned_text = re.sub(r'\\sphinxstylestrong', r'\\textbf', text)  # Remove \sphinxstylestrong{}
        cleaned_text = re.sub(r'\\sphinxAtStartPar', '', cleaned_text)  # Remove \sphinxAtStartPar
        cleaned_text = re.sub(r'\\sphinxmidrule', r'\\hline', cleaned_text)  # Change \sphinxmidrule to \hline
        cleaned_text = re.sub(r'\\sphinxtoprule', r'\\hline', cleaned_text)  # Change \sphinxtoprule to \hline
        cleaned_text = re.sub(r'\\sphinxhline', r'\\hline', cleaned_text)  # Change \sphinxhline to \hline
        return cleaned_text

    def table_replacement(match):
        col_spec = match.group(1)
        table_body = match.group(2)

        # Convert tabulary column spec to longtable format
        col_spec = map_column_spec(col_spec)

        rows = []
        current_row_lines = []

        for line in table_body.splitlines():
            stripped_line = line.strip()
            if not stripped_line:
                continue  # skip empty lines
            current_row_lines.append(stripped_line)

            if stripped_line.endswith(r'\\'):
                # Join all accumulated lines, remove trailing '\\'
                full_row = ' '.join(current_row_lines)[:-2].strip()
                # Clean up Sphinx-specific commands
                full_row = clean_sphinx_commands(full_row)
                cells = [cell.strip() for cell in re.split(r'(?<!\\)&', full_row)]
                rows.append(cells)
                current_row_lines = []  # reset buffer for next row

        # Now generate longtable using the converted column spec
        longtable_tex = encode_longtable(rows, col_spec)
        return longtable_tex

    new_tex_content, count = table_pattern.subn(table_replacement, tex_content)

    if count == 0:
        print("No tabulary tables found.")
        return True

    with open(tex_file, 'w', encoding='utf-8') as file:
        file.write(new_tex_content)

    print(f"Converted {count} tabulary table(s) to longtable.")
    return True

def run_latexmk(tex_file):
    build_dir = os.path.dirname(tex_file)
    tex_filename = os.path.basename(tex_file)
    print("Running latexmk...")
    try:
        subprocess.run(["latexmk", "-silent", "-pdf", tex_filename], check=True, cwd=build_dir)
        print("PDF build complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error running latexmk: {e}")

def main():
    build_folder = '_build'
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)
        print(f"Removed directory: {build_folder}")

    if not run_sphinx_build():
        return

    tex_file = '_build/en/emeditor.tex'

    if not remove_svg_from_tex(tex_file):
        return

    if not convert_tabulary_to_longtable(tex_file):
        return

    if not run_latexmk(tex_file):
        return

    print("All steps completed successfully.")

if __name__ == '__main__':
    main()
