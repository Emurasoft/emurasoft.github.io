# \[言語サーバー\] ページ

**\[言語サーバー\]** ページでは、EmEditor の言語サーバーに関するプロパティを設定できます。

### \[言語サーバー プロトコルを有効にする (試験的)\] チェック ボックス

これがチェックされていると、言語サーバー プロトコルを有効にします。

### \[文書タイプ\] ドロップダウン リスト ボックス

使用する言語サーバーを指定します。HTML、CSS、JavaScript、Perl サーバーは標準でインストールされていて使用可能です。他の言語は、追加のインストールが必要になります。以下の「言語サーバーのインストール」を参照してインストールしてください。

### \[リセット\] ボタン

設定を既定にします。

## 言語サーバーのインストール

### C/C++

[clangd](https://clangd.llvm.org/installation) をインストールし、 [project setup](https://clangd.llvm.org/installation#project-setup) の説明に従い、 `compile_commands.json` ファイルを作成します。コマンド プロンプトを開き、 `clangd ` を呼んで、インストールをテストします。 `clangd ` は、CMake と Bazel ベースのプロジェクトのみをサポートします。

### Python

pip を使用して [Python LSP Server](https://github.com/python-lsp/python-lsp-server) をインストールします。コマンド プロンプトで `python -m pylsp` を実行してインストールをテストします。

### HTML, CSS, JavaScript, and Perl

これらのサーバーは EmEditor に標準でインストールされています。次の一覧は、それらのソース リポジトリへのリンクです。

- HTML と CSS: [VSCode extensions](https://github.com/microsoft/vscode)
- JavaScript: [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server)
- Perl: [Perl Navigator Language Server](https://github.com/bscan/PerlNavigator)
