# 「語言伺服器」頁面

啟用語言伺服器通訊協定可啟用以下功能：

- 停留工具提示
- **搜尋** 功能表上的 **搜尋符號**
- 允許選擇 **語言伺服器通訊協定** 作為 **語法檢查** 的 **文檔類型**

## 

### 「啟用語言伺服器通訊協定（實驗性）」核取方塊

用語言伺服器通訊協定啟用停留工具提示。

### 「文檔類型」下拉清單方塊

指定要使用的語言伺服器。HTML、CSS、JavaScript 和 Perl 服務器隨 EmEditor 安裝並可以使用。其他語言伺服器需要額外的安裝步驟。有關安裝語言伺服器的信息，請參閱下面的「語言伺服器安裝」部分。

### 「重設」按鈕

重設為預設設定。會顯示 [**重設** 對話方塊](../reset/index) 並讓你能從另一個組態複製設定。

## 語言伺服器安裝

### C/C++

安裝 [clangd](https://clangd.llvm.org/installation)。通過打開命令提示字元並調用 `clangd` 來測試安裝。 它支持基於 CMake 和 Bazel 的項目。您需要按照上述頁面上的項目設定步驟來生成 `compile_commands.json` 檔案。

### Python

用 pip 安裝 [Python LSP Server](https://github.com/python-lsp/python-lsp-server)。在命令提示字元中使用 `python -m pylsp` 測試安裝。

### HTML，CSS，JavaScript，JSON 和 Perl

EmEditor 內置了這些服務器。以下清單提供了指向其源儲存機制的連結。

- HTML，CSS 和 JSON： [VSCode extensions](https://github.com/microsoft/vscode)
- JavaScript： [TypeScript Language Server](https://github.com/typescript-language-server/typescript-language-server)
- Perl： [Perl Navigator Language Server](https://github.com/bscan/PerlNavigator)

