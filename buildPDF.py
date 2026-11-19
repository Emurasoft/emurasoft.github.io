import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PDF_LANGUAGES = ('en', 'ja')
BUILD_ROOT = Path('_build')
TEX_NAME = 'emeditor.tex'

SPHINX_TO_LATEX = {
    r'\sphinxstylestrong': r'\textbf',
    r'\sphinxAtStartPar': '',
    r'\sphinxmidrule': r'\hline',
    r'\sphinxtoprule': r'\hline',
    r'\sphinxhline': r'\hline',
}

EMOJI_RANGES = (
    (0x1F300, 0x1F5FF),
    (0x1F600, 0x1F64F),
    (0x1F680, 0x1F6FF),
    (0x1F700, 0x1F77F),
    (0x1F780, 0x1F7FF),
    (0x1F900, 0x1F9FF),
    (0x1FA00, 0x1FA6F),
    (0x1FA70, 0x1FAFF),
)

SYMBOL_RANGES = (
    (0x1F800, 0x1F8FF),
)


def run_sphinx_build(language: str) -> bool:
    """Run sphinx-build to generate LaTeX files for one language."""
    print(f"[{language}] Running sphinx-build...")
    env = {**os.environ, 'PROJECT': language, 'SPHINX_BUILDER': 'latex'}
    output_dir = BUILD_ROOT / language
    result = subprocess.run(
        [sys.executable, '-m', 'sphinx', '--jobs', 'auto', '-b', 'latex', '.', str(output_dir)],
        capture_output=True, text=True, encoding='utf-8', errors='replace', env=env
    )
    if result.returncode != 0:
        print(f"[{language}] Error running sphinx-build:")
        print(result.stderr or result.stdout)
        return False
    print(f"[{language}] Sphinx build complete.")
    return True


def read_tex_file(tex_file: Path) -> str | None:
    """Read a TeX file, or report the error and return None."""
    try:
        return tex_file.read_text(encoding='utf-8')
    except OSError as error:
        print(f"Error reading {tex_file}: {error}")
        return None


def write_tex_file(tex_file: Path, content: str) -> bool:
    """Write content to a TeX file."""
    try:
        tex_file.write_text(content, encoding='utf-8')
    except OSError as error:
        print(f"Error writing to {tex_file}: {error}")
        return False
    return True


def remove_svg_from_tex(content: str) -> str:
    """Remove SVG image references from the content."""
    lines = [line for line in content.splitlines()
             if not (r'\sphinxincludegraphics' in line and '.svg' in line)]
    print("SVG image references removed.")
    return '\n'.join(lines)


def convert_tabulary_to_longtable(content: str) -> str:
    """Convert tabulary tables to longtable format."""
    new_content, count = replace_tabulary_tables(content)

    if count == 0:
        print("No tabulary tables found.")
    else:
        print(f"Converted {count} tabulary table(s) to longtable.")

    return new_content


def replace_tabulary_tables(tex_content: str) -> tuple[str, int]:
    """Identifies and replaces tabulary tables in the LaTeX content."""
    table_pattern = re.compile(
        r'\\begin\{tabulary\}\{.*?\}\[.*?\]\{(.*?)\}(.*?)\\end\{tabulary\}',
        re.DOTALL
    )

    def table_replacement(match: re.Match[str]) -> str:
        col_spec = map_column_spec(match.group(1))
        rows = parse_table_body(match.group(2))
        return encode_longtable(rows, col_spec)

    return table_pattern.subn(table_replacement, tex_content)


def map_column_spec(tab_spec: str) -> str:
    """Maps the column specification for tabulary to longtable."""
    num_columns = tab_spec.count('T')

    if num_columns == 0:
        column_width = '4in'
    else:
        # Standard US Letter width with 1-inch margins, minus a small
        # adjustment per column to account for borders and spacing.
        usable_width = 8.5 - 2 * 1
        adjusted_width = max(0.25, usable_width / num_columns - num_columns * 0.0045)
        column_width = f'{adjusted_width:.2f}in'

    columns = [f'p{{{column_width}}}' if col == 'T' else col for col in tab_spec]
    return '|' + '|'.join(columns) + '|'


def parse_table_body(table_body: str) -> list[list[str]]:
    """Parses the table body into rows and cells."""
    rows = []
    current_row = []

    for line in table_body.splitlines():
        line = line.strip()
        if not line:
            continue

        current_row.append(line)

        if line.endswith(r'\\'):  # End of row
            row = ' '.join(current_row)[:-2].strip()
            row = clean_sphinx_commands(row)
            rows.append([cell.strip() for cell in re.split(r'(?<!\\)&', row)])
            current_row = []

    return rows


def clean_sphinx_commands(text: str) -> str:
    """Replace Sphinx commands with LaTeX equivalents."""
    for sphinx_command, latex in SPHINX_TO_LATEX.items():
        text = text.replace(sphinx_command, latex)

    return text


def encode_longtable(rows: list[list[str]], col_spec: str = 'll') -> str:
    """Create longtable LaTeX code from rows and column specification."""
    body = '\n'.join(' & '.join(row) + r'\\' for row in rows)
    return '\n'.join([
        f'\\begin{{longtable}}{{{col_spec}}}',
        body,
        '\\end{longtable}',
    ])


def in_ranges(char: str, ranges: tuple[tuple[int, int], ...]) -> bool:
    """Return whether the character's code point falls in any range."""
    codepoint = ord(char)
    return any(start <= codepoint <= end for start, end in ranges)


def wrap_special_chars_in_tex(content: str) -> str:
    """Wrap emoji and symbol characters with appropriate LaTeX commands."""
    new_content = []
    emoji_count = 0
    symbol_count = 0

    for char in content:
        if in_ranges(char, EMOJI_RANGES):
            new_content.append(f"\\emoji{{{char}}}")
            emoji_count += 1
        elif in_ranges(char, SYMBOL_RANGES):
            new_content.append(f"\\symbolchar{{{char}}}")
            symbol_count += 1
        else:
            new_content.append(char)

    print(f"Wrapped {emoji_count} emoji(s) with \\emoji{{}} and {symbol_count} symbol(s) with \\symbolchar{{}}.")
    return ''.join(new_content)


def postprocess_tex(tex_file: Path, language: str) -> bool:
    """Apply the TeX transformations to the generated file."""
    print(f"[{language}] Transforming {tex_file.name}...")
    content = read_tex_file(tex_file)
    if content is None:
        return False

    content = remove_svg_from_tex(content)
    content = convert_tabulary_to_longtable(content)
    content = wrap_special_chars_in_tex(content)

    return write_tex_file(tex_file, content)


def run_latexmk(tex_file: Path, language: str) -> bool:
    """Run latexmk to build the PDF."""
    print(f"[{language}] Running latexmk...")
    try:
        subprocess.run(
            ["latexmk", "-silent", "-lualatex", tex_file.name],
            check=True, cwd=tex_file.parent)
    except subprocess.CalledProcessError as error:
        print(f"[{language}] Error running latexmk: {error}")
        log_path = tex_file.with_suffix('.log')
        if not log_path.is_file():
            print(f"[{language}] Log file not found: {log_path}")
            return False

        lines = log_path.read_text(encoding='utf-8', errors='replace').splitlines()
        print(f"[{language}] Last 200 lines of {log_path.name}:")
        if len(lines) > 200:
            print(f"(showing last 200 of {len(lines)} lines)")
        print('\n'.join(lines[-200:]))
        return False

    print(f"[{language}] PDF build complete.")
    return True


def build_pdf(language: str) -> bool:
    """Build one language's PDF and stage it in the build root."""
    build_dir = BUILD_ROOT / language
    shutil.rmtree(build_dir, ignore_errors=True)

    if not run_sphinx_build(language):
        return False

    tex_file = build_dir / TEX_NAME
    if not postprocess_tex(tex_file, language):
        return False

    if not run_latexmk(tex_file, language):
        return False

    pdf_file = tex_file.with_suffix('.pdf')
    if not pdf_file.is_file() or pdf_file.stat().st_size == 0:
        print(f"[{language}] Error: {pdf_file} was not produced.")
        return False

    staged_pdf = BUILD_ROOT / f'emeditor-{language}.pdf'
    shutil.copy2(pdf_file, staged_pdf)
    print(f"[{language}] PDF staged as {staged_pdf}.")
    return True


def parse_languages(argv: list[str]) -> list[str]:
    """Validate command line language arguments."""
    if not argv:
        return list(PDF_LANGUAGES)

    unknown = [arg for arg in argv if arg not in PDF_LANGUAGES]
    if unknown:
        print(f"Unknown language(s): {', '.join(unknown)}")
        print(f"Usage: python buildPDF.py [{'|'.join(PDF_LANGUAGES)} ...]")
        sys.exit(2)

    return list(dict.fromkeys(argv))


def main(languages: list[str]) -> None:
    # Remove stale staged PDFs so a failed run cannot leave an old build behind
    for language in languages:
        (BUILD_ROOT / f'emeditor-{language}.pdf').unlink(missing_ok=True)

    print("Note: the requested languages' _build/<language> directories are replaced; other _build content is kept.")
    for language in languages:
        print(f"=== Building the {language} PDF ===")
        if not build_pdf(language):
            print(f"Error: the {language} PDF build failed.")
            sys.exit(1)

    print("All steps completed successfully.")


if __name__ == '__main__':
    main(parse_languages(sys.argv[1:]))
