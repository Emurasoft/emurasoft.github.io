# Language Server page

The **Language Server** page allows you to set properties related to language server.

## 

### Enable Language Server Protocol check box

Enabling Language Server Protocol turns on the following features:

- Hover tooltips when the **Show hover tooltips** check box is set.
- **Search Symbols** in the **Search** menu
- Allows selecting **Language Server Protocol** as the **Document Type** for **Syntax Check**

### Document Type drop-down list box

Specifies the language server to use. The HTML, CSS, JavaScript, and Perl servers are installed with EmEditor and are ready to use. Other language servers require additional steps to install. See the "Language Server installation" section below for information on installing language servers.

### Show hover tooltip check box

Shows hover tooltips.

### Show completion list check box

Shows completion list.

### Reset button

Resets to default settings. The [**Reset** dialog box](../reset/index) will be displayed and will allow you to copy from another configuration.

## Language Server installation

### C/C++

Install [clangd](https://clangd.llvm.org/installation) and follow the [project setup](https://clangd.llvm.org/installation#project-setup) instructions to generate the `compile_commands.json` file. Test the installation by opening Command Prompt and calling `clangd --version`. clangd only supports CMake and Bazel-based projects.

### Python

Use pip to install [Python LSP Server](https://github.com/python-lsp/python-lsp-server). Test the installation with `python -m pylsp --help` in Command Prompt.

### HTML, CSS, JavaScript, JSON, and Perl

These servers are built-in with EmEditor. The following list provides links to their source repositories.

- HTML, CSS, and JSON: [VSCode extensions](https://github.com/microsoft/vscode)
- JavaScript: [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server)
- Perl: [Perl Navigator Language Server](https://github.com/bscan/PerlNavigator)

