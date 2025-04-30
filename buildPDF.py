import os
import subprocess
import shutil
import re
import sys

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
    header = "\\begin{longtable}{" + col_spec + "}"
    body = "\n".join(
        " & ".join(row) + r"\\"
        for row in rows
    )
    footer = "\\end{longtable}"
    return "\n".join([header, body, footer])

def convert_tabulary_to_longtable(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    with open(tex_file, 'r', encoding='utf-8') as file:
        tex_content = file.read()

    new_tex_content, count = replace_tabulary_tables(tex_content)

    if count == 0:
        print("No tabulary tables found.")
        return True

    with open(tex_file, 'w', encoding='utf-8') as file:
        file.write(new_tex_content)

    print(f"Converted {count} tabulary table(s) to longtable.")
    return True


def replace_tabulary_tables(tex_content):
    """Identifies and replaces tabulary tables in the LaTeX content."""
    table_pattern = re.compile(
        r'\\begin\{tabulary\}\{.*?\}\[.*?\]\{(.*?)\}(.*?)\\end\{tabulary\}',
        re.DOTALL
    )

    def table_replacement(match):
        col_spec = match.group(1)
        table_body = match.group(2)
        col_spec = map_column_spec(col_spec)
        rows = parse_table_body(table_body)
        return encode_longtable(rows, col_spec)

    return table_pattern.subn(table_replacement, tex_content)


def map_column_spec(tab_spec):
    """Maps the column specification for tabulary to longtable."""
    page_width = 8.5  # Example: standard US Letter width in inches
    margin_left_right = 1  # Example: 1-inch margin on both sides
    usable_width = page_width - 2 * margin_left_right
    num_columns = sum(1 for col in tab_spec if col == 'T')

    if num_columns > 0:
        column_width = usable_width / num_columns
        column_width = f"{column_width:.2f}in"
    else:
        column_width = '1in'

    return '|' + '|'.join(f'p{{{column_width}}}' if col == 'T' else col for col in tab_spec) + '|'


def parse_table_body(table_body):
    """Parses the table body into rows and cells."""
    rows = []
    current_row_lines = []

    for line in table_body.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue

        current_row_lines.append(stripped_line)

        if stripped_line.endswith(r'\\'):  # End of row
            full_row = ' '.join(current_row_lines)[:-2].strip()
            full_row = clean_sphinx_commands(full_row)
            cells = [cell.strip() for cell in re.split(r'(?<!\\)&', full_row)]
            rows.append(cells)
            current_row_lines = []

    return rows


def clean_sphinx_commands(text):
    replacements = {
        r'\sphinxstylestrong': r'\textbf',
        r'\sphinxAtStartPar': '',
        r'\sphinxmidrule': r'\hline',
        r'\sphinxtoprule': r'\hline',
        r'\sphinxhline': r'\hline'
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def encode_longtable(rows, col_spec='ll'):
    """Encodes rows into a LaTeX longtable format."""
    header = "\\begin{longtable}{" + col_spec + "}"
    body = "\n".join(" & ".join(row) + r"\\" for row in rows)
    footer = "\\end{longtable}"
    return "\n".join([header, body, footer])

def wrap_emojis_in_tex(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    emoji_pattern = re.compile(
        r'(['
        '\U00002600-\U000026FF'
        '\U00002700-\U000027BF'
        '\U0001F300-\U0001F5FF'
        '\U0001F600-\U0001F64F'
        '\U0001F680-\U0001F6FF'
        '\U0001F700-\U0001F77F'
        '\U0001F780-\U0001F7FF'
        '\U0001F800-\U0001F8FF'
        '\U0001F900-\U0001F9FF'
        '\U0001FA00-\U0001FA6F'
        '\U0001FA70-\U0001FAFF'
        '])'
    )

    with open(tex_file, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content, count = emoji_pattern.subn(r'\\emoji{\1}', content)

    with open(tex_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Wrapped {count} emoji(s) with \\emoji{{}}.")
    return True

def wrap_symbols_in_tex(tex_file):
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    # Supplemental Arrows-C: U+1F800–U+1F8FF (🠀–🠿)
    symbol_pattern = re.compile(
        r'([\U0001F800-\U0001F8FF])'
    )

    with open(tex_file, 'r', encoding='utf-8') as file:
        content = file.read()

    new_content, count = symbol_pattern.subn(r'\\symbolchar{\1}', content)

    with open(tex_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Wrapped {count} symbol character(s) with \\symbolchar{{}}.")
    return True

def run_latexmk(tex_file):
    build_dir = os.path.dirname(tex_file)
    tex_filename = os.path.basename(tex_file)
    print("Running latexmk...")
    try:
        subprocess.run(["latexmk", "-silent", "-lualatex", tex_filename], check=True, cwd=build_dir)
    except subprocess.CalledProcessError as e:
        print(f"Error running latexmk: {e}")
        log_path = os.path.join(build_dir, 'emeditor.log')
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                print("emeditor.log contents:")
                print(log_file.read())
        else:
            print(f"Log file not found: {log_path}")
        return False

    print("PDF build complete.")
    return True

def main():
    build_folder = '_build'
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)
        print(f"Removed directory: {build_folder}")

    if not run_sphinx_build():
        sys.exit(1)

    tex_file = '_build/en/emeditor.tex'

    if not remove_svg_from_tex(tex_file):
        sys.exit(1)

    if not convert_tabulary_to_longtable(tex_file):
        sys.exit(1)

    if not wrap_emojis_in_tex(tex_file):
        sys.exit(1)

    if not wrap_symbols_in_tex(tex_file):
        sys.exit(1)

    if not run_latexmk(tex_file):
        sys.exit(1)

    print("All steps completed successfully.")

if __name__ == '__main__':
    main()