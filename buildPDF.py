import os
import re
import shutil
import subprocess
import sys
from typing import List, Tuple, Match, Optional

PDF_LANGUAGES = ('en', 'ja')
BUILD_ROOT = '_build'
TEX_NAME = 'emeditor.tex'

def run_sphinx_build(language: str) -> bool:
    """Run sphinx-build to generate LaTeX files for one language."""
    print(f"[{language}] Running sphinx-build...")
    env = dict(os.environ)
    env['PROJECT'] = language
    env['SPHINX_BUILDER'] = 'latex'
    output_dir = os.path.join(BUILD_ROOT, language)
    result = subprocess.run(
        [sys.executable, '-m', 'sphinx', '--jobs', 'auto', '-b', 'latex', '.', output_dir],
        capture_output=True, text=True, encoding='utf-8', errors='replace', env=env
    )
    if result.returncode != 0:
        print(f"[{language}] Error running sphinx-build:")
        print(result.stderr if result.stderr else result.stdout)
        return False
    print(f"[{language}] Sphinx build complete.")
    return True

def read_tex_file(tex_file: str) -> Optional[str]:
    """Read a TeX file and return its contents as a string."""
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return None

    try:
        with open(tex_file, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {tex_file}: {e}")
        return None

def write_tex_file(tex_file: str, content: str) -> bool:
    """Write content to a TeX file."""
    try:
        with open(tex_file, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to {tex_file}: {e}")
        return False

def remove_svg_from_tex(content: str) -> str:
    """Remove SVG image references from the content."""
    lines = content.splitlines()
    filtered_lines = [line for line in lines
                     if not (r'\sphinxincludegraphics' in line and '.svg' in line)]
    print("SVG image references removed.")
    return '\n'.join(filtered_lines)

def convert_tabulary_to_longtable(content: str) -> str:
    """Convert tabulary tables to longtable format."""
    new_content, count = replace_tabulary_tables(content)

    if count == 0:
        print("No tabulary tables found.")
    else:
        print(f"Converted {count} tabulary table(s) to longtable.")

    return new_content

def replace_tabulary_tables(tex_content: str) -> Tuple[str, int]:
    """Identifies and replaces tabulary tables in the LaTeX content."""
    table_pattern = re.compile(
        r'\\begin\{tabulary\}\{.*?\}\[.*?\]\{(.*?)\}(.*?)\\end\{tabulary\}',
        re.DOTALL
    )

    def table_replacement(match: Match[str]) -> str:
        col_spec = match.group(1)
        table_body = match.group(2)
        col_spec = map_column_spec(col_spec)
        rows = parse_table_body(table_body)
        return encode_longtable(rows, col_spec)

    return table_pattern.subn(table_replacement, tex_content)

def map_column_spec(tab_spec: str) -> str:
    """Maps the column specification for tabulary to longtable."""
    page_width = 8.5  # Example: standard US Letter width in inches
    margin_left_right = 1  # Example: 1-inch margin on both sides
    usable_width = page_width - 2 * margin_left_right
    num_columns = sum(1 for col in tab_spec if col == 'T')

    if num_columns > 0:
        base_column_width = usable_width / num_columns

        # Linear adjustment factor per column to account for borders/spacing
        factor = 0.0045

        adjusted_width = base_column_width - (num_columns * factor)
        adjusted_width = max(0.25, adjusted_width)

        column_width_str = f"{adjusted_width:.2f}in"
    else:
        column_width_str = '4in'

    return '|' + '|'.join(f'p{{{column_width_str}}}' if col == 'T' else col for col in tab_spec) + '|'

def parse_table_body(table_body: str) -> List[List[str]]:
    """Parses the table body into rows and cells."""
    rows: List[List[str]] = []
    current_row_lines: List[str] = []

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

def clean_sphinx_commands(text: str) -> str:
    """Replace Sphinx commands with LaTeX equivalents."""
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

def encode_longtable(rows: List[List[str]], col_spec: str = 'll') -> str:
    """Create longtable LaTeX code from rows and column specification."""
    header = "\\begin{longtable}{" + col_spec + "}"
    body = "\n".join(
        " & ".join(row) + r"\\"
        for row in rows
    )
    footer = "\\end{longtable}"
    return "\n".join([header, body, footer])

emoji_ranges: List[Tuple[int, int]] = [
    (0x1F300, 0x1F5FF),
    (0x1F600, 0x1F64F),
    (0x1F680, 0x1F6FF),
    (0x1F700, 0x1F77F),
    (0x1F780, 0x1F7FF),
    (0x1F900, 0x1F9FF),
    (0x1FA00, 0x1FA6F),
    (0x1FA70, 0x1FAFF),
]

symbol_ranges: List[Tuple[int, int]] = [
    (0x1F800, 0x1F8FF),
]

def is_emoji(char: str) -> bool:
    """Check if a character is an emoji."""
    codepoint = ord(char)
    return any(start <= codepoint <= end for start, end in emoji_ranges)

def is_symbol(char: str) -> bool:
    """Check if a character is a symbol that needs special handling."""
    codepoint = ord(char)
    return any(start <= codepoint <= end for start, end in symbol_ranges)

def wrap_special_chars_in_tex(content: str) -> str:
    """Wrap emoji and symbol characters with appropriate LaTeX commands."""
    new_content: List[str] = []
    emoji_count: int = 0
    symbol_count: int = 0

    for char in content:
        if is_emoji(char):
            new_content.append(f"\\emoji{{{char}}}")
            emoji_count += 1
        elif is_symbol(char):
            new_content.append(f"\\symbolchar{{{char}}}")
            symbol_count += 1
        else:
            new_content.append(char)

    print(f"Wrapped {emoji_count} emoji(s) with \\emoji{{}} and {symbol_count} symbol(s) with \\symbolchar{{}}.")
    return ''.join(new_content)

def postprocess_tex(tex_file: str, language: str) -> bool:
    """Apply the TeX transformations to the generated file."""
    print(f"[{language}] Transforming {os.path.basename(tex_file)}...")
    content = read_tex_file(tex_file)
    if content is None:
        return False

    content = remove_svg_from_tex(content)
    content = convert_tabulary_to_longtable(content)
    content = wrap_special_chars_in_tex(content)

    return write_tex_file(tex_file, content)

def run_latexmk(tex_file: str, language: str) -> bool:
    """Run latexmk to build the PDF."""
    build_dir = os.path.dirname(tex_file)
    tex_filename = os.path.basename(tex_file)
    print(f"[{language}] Running latexmk...")
    try:
        subprocess.run(["latexmk", "-silent", "-lualatex", tex_filename], check=True, cwd=build_dir)
    except subprocess.CalledProcessError as e:
        print(f"[{language}] Error running latexmk: {e}")
        log_path = os.path.splitext(tex_file)[0] + '.log'
        if os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8', errors='replace') as log_file:
                lines = log_file.read().splitlines()
            print(f"[{language}] Last 200 lines of {os.path.basename(log_path)}:")
            if len(lines) > 200:
                print(f"(showing last 200 of {len(lines)} lines)")
            print('\n'.join(lines[-200:]))
        else:
            print(f"[{language}] Log file not found: {log_path}")
        return False

    print(f"[{language}] PDF build complete.")
    return True

def build_pdf(language: str) -> bool:
    """Build one language's PDF and stage it in the build root."""
    build_dir = os.path.join(BUILD_ROOT, language)
    shutil.rmtree(build_dir, ignore_errors=True)

    if not run_sphinx_build(language):
        return False

    tex_file = os.path.join(build_dir, TEX_NAME)
    if not postprocess_tex(tex_file, language):
        return False

    if not run_latexmk(tex_file, language):
        return False

    pdf_file = os.path.splitext(tex_file)[0] + '.pdf'
    if not os.path.exists(pdf_file) or os.path.getsize(pdf_file) == 0:
        print(f"[{language}] Error: {pdf_file} was not produced.")
        return False

    staged_pdf = os.path.join(BUILD_ROOT, f'emeditor-{language}.pdf')
    shutil.copy2(pdf_file, staged_pdf)
    print(f"[{language}] PDF staged as {staged_pdf}.")
    return True

def parse_languages(argv: List[str]) -> List[str]:
    """Validate command line language arguments."""
    if not argv:
        return list(PDF_LANGUAGES)

    unknown = [arg for arg in argv if arg not in PDF_LANGUAGES]
    if unknown:
        print(f"Unknown language(s): {', '.join(unknown)}")
        print(f"Usage: python buildPDF.py [{'|'.join(PDF_LANGUAGES)} ...]")
        sys.exit(2)

    languages: List[str] = []
    for arg in argv:
        if arg not in languages:
            languages.append(arg)
    return languages

def main(languages: List[str]) -> None:
    # Remove stale staged PDFs so a failed run cannot leave an old build behind
    for language in languages:
        staged_pdf = os.path.join(BUILD_ROOT, f'emeditor-{language}.pdf')
        if os.path.exists(staged_pdf):
            os.remove(staged_pdf)

    print("Note: the requested languages' _build/<language> directories are replaced; other _build content is kept.")
    for language in languages:
        print(f"=== Building the {language} PDF ===")
        if not build_pdf(language):
            print(f"Error: the {language} PDF build failed.")
            sys.exit(1)

    print("All steps completed successfully.")

if __name__ == '__main__':
    main(parse_languages(sys.argv[1:]))
