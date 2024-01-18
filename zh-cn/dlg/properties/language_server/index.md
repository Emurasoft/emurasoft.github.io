# “语言服务器”页面

**语言服务器**让你能设置与语言服务器相关的属性。

## 

### “启用语言服务器协议”复选框

启用语言服务器协议可启用以下功能：

- 悬停工具提示在勾选**显示悬停工具提示**复选框后
- **搜索**菜单上的**搜索符号**
- 允许选择**语言服务器协议**作为**语法检查**的**文档类型**

### “文档类型”下拉列表框

指定要使用的语言服务器。HTML、CSS、JavaScript 和 Perl 服务器随 EmEditor 安装并可以使用。其他语言服务器需要额外的安装步骤。有关安装语言服务器的信息，请参阅下面的“语言服务器安装”部分。

### “显示悬停工具提示”复选框

显示悬停工具提示。

### “显示完成列表”复选框

显示完成列表。

### 「重置」按钮

重置为默认设定。会显示[**重置**对话框](../reset/index)并让你能从另一个配置复制设定。

## 语言服务器安装

### C/C++

安装 [clangd](https://clangd.llvm.org/installation)。通过打开命令提示符并调用 `clangd --version` 来测试安装。 它支持基于 CMake 和 Bazel 的项目。您需要按照上述页面上的项目设置步骤来生成 `compile_commands.json` 文件。

### Python

用 pip 安装 [Python LSP Server](https://github.com/python-lsp/python-lsp-server)。在命令提示符中使用 `python -m pylsp --help` 测试安装。

### HTML，CSS，JavaScript，JSON 和 Perl

EmEditor 内置了这些服务器。以下列表提供了指向其源存储库的链接。

- HTML，CSS 和 JSON： [VSCode extensions](https://github.com/microsoft/vscode)
- JavaScript： [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server)
- Perl： [Perl Navigator Language Server](https://github.com/bscan/PerlNavigator)

