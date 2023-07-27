# 插入字符 (�̳�)

要用宏来插入字符，用[Text 属性](../selection/selection_text)。你可以按下列步骤修改教程文件:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
被添加到第二行的[NewLine 方法](../selection/selectionnewline) 会在光标位置插入一个新的行。在第三行的代码会在字符串起始位置插入一个 tab 字符。一个 tab 字符在 JavaScript 中由 "\\t" 表示，在 VBScript 中由 Chr(9) 表示。你同样能用 VBScript 常数，vbTab，作为一个 tab 字符。
下列表格列出了在 JavaScript 和 VBScript 常用的转义序列。
```

### \[JavaScript\]

```
|     |     |     |
| --- | --- | --- |
| \\b | \\u0008 | 后退键。 |
| \\t | \\u0009 | 水平 tab。 |
| \\n | \\u000a | 新行。 |
| \\f | \\u000c | 换页。 |
| \\r | \\u000d | 回车。 |
| \\" | \\u0022 | 双引号。 |
| \\' | \\u0027 | 单引号。 |
| \\\ | \\u005c | 反斜杠。 |
| \\xXX |  | 由两个十六进制数指定的含编码的 Latin-1 字符。 |
| \\uXXXX |  | 由四个十六进制数指定的含编码的 Unicode 字符。 |
```

### ![](../../images/g.gif) 参考:  [JScript \ 特殊字符 (Microsoft MSDN Library)](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Lexical_grammar\#%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9B%B4%E6%8E%A5%E9%87%8F)

### \[VBScript\]

```
|     |     |     |
| --- | --- | --- |
| vbCr | Chr(13) | 回车。 |
| vbCrLf | Chr(13) & Chr(10) | 回车 \+ 新行组合。 |
| vbFormFeed | Chr(12) | 换页。 |
| vbLf | Chr(10) | 新行。 |
| vbNewLine | Chr(13) & Chr(10) or Chr(10) | 特定平台的新行字符。相当于 Windows 中的 vbCrLf。 |
| vbTab | Chr(9) | 水平 tab。 |
| vbVerticalTab | Chr(11) | 垂直 tab。 |
```

### ![](../../images/g.gif) 参考:  [VBScript 字符串常数 (Microsoft MSDN Library)](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/hh277t8e(v=vs.84))

## 提示

行尾端以一个 \\r (CR) 和一个 \\n (LF) 的组合结尾。CR 和 LF 使用不同方式。例如，如果你写:

document.selection.Text = "\\n";

插入的仅仅是回车符 (LF)，而不是 Windows 行尾端的惯例。当你在 EmEditor 中按回车键时，EmEditor 会插入该行所用的行尾端方式（仅 CR，仅 LF，或 CR+LF）。如果你想要在按回车键时与在 EmEditor 中有相同的行为，我们建议你用
[NewLine 方法](../selection/selection_newline)
或[writeln 方法](../document/document_writeln)。

## 下一主题:
