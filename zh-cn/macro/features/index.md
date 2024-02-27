# 功能

EmEditor Professional 让你能用 JavaScript 或 VBScript 创建功能丰富的宏。宏的功能包括:

```{toctree}
:maxdepth: 1
can_script_all
keystroke_mouse
macro_ide
script_language
separate_design
windows_scripting_host
```

## 注意

要利用现代 JavaScript/ECMAScript 中的许多新方法，请选择 V8 引擎。要激活 V8，请在 **自定义宏** 对话框中的 [**选项** 页面](../../dlg/macro_customize/options/index) 上设置 **使用 V8 作为 JavaScript 引擎** 复选框， 或者在宏的开头插入 **[#language](../directive/language) = "V8"** 。

如果不选择 V8，EmEditor 宏将在 JScript 5.8（对应于 Internet Explorer 8.0）上运行，这意味着 EmEditor 宏将不支持 JScript 5.8 之后引入的方法。确保您打算使用的方法与版本要求兼容。