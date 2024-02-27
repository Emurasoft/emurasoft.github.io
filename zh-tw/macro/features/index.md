# 功能

EmEditor Professional 讓您能用 JavaScript 或 VBScript 創建功能豐富的巨集。巨集的功能包括:

```{toctree}
:maxdepth: 1
can_script_all
keystroke_mouse
macro_ide
script_language
separate_design
windows_scripting_host
```

## 註意

要利用現代 JavaScript/ECMAScript 中的許多新方法，請選擇 V8 引擎。要啟動 V8，請在 **自訂巨集** 對話方塊中的 [**選項** 頁面](../../dlg/macro_customize/options/index) 上設定 **使用 V8 作為 JavaScript 引擎** 核取方塊， 或者在巨集的開頭插入 **[#language](../directive/language) = "V8"** 。

如果不選擇 V8，EmEditor 巨集將在 JScript 5.8（對應於 Internet Explorer 8.0）上運行，這意味著 EmEditor 巨集將不支援 JScript 5.8 之後引入的方法。確保您打算使用的方法與版本要求兼容。