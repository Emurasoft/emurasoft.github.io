import os
import subprocess

def run_sphinx_build():
    """Run the Sphinx build command to generate the LaTeX files."""
    print("Running sphinx-build...")
    result = subprocess.run(['sphinx-build', '-b', 'latex', '.', '_build/en'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running sphinx-build: {result.stderr}")
        return False
    print("Sphinx build complete.")
    return True

def remove_svg_from_tex(tex_file):
    """Remove lines with \sphinxincludegraphics referencing .svg files."""
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} does not exist.")
        return False

    with open(tex_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(tex_file, 'w', encoding='utf-8') as file:
        for line in lines:
            if not (line.strip().startswith(r'\sphinxincludegraphics') and '.svg' in line):
                file.write(line)

    print("SVG image references removed from the LaTeX file.")
    return True

def run_latexmk(tex_file):
    """Run latexmk to compile the LaTeX file to PDF."""
    build_dir = os.path.dirname(tex_file)
    tex_filename = os.path.basename(tex_file)
    print("Running latexmk...")
    try:
        subprocess.run(["latexmk", "-pdf", tex_filename], check=True, cwd=build_dir)
        print("PDF build complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error running latexmk: {e}")

def main():
    # Step 1: Run Sphinx to generate LaTeX files
    if not run_sphinx_build():
        return

    tex_file = '_build/en/emeditor.tex'

    # Step 2: Remove SVG references from the LaTeX file
    if not remove_svg_from_tex(tex_file):
        return

    # Step 3: Run latexmk to compile the LaTeX file into PDF
    if not run_latexmk(tex_file):
        return

    print("All steps completed successfully.")

if __name__ == '__main__':
    main()
