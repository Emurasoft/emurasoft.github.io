# 插入字元 (�е{)

要用巨集來插入字元，用 **[Text 屬性](../selection/selection_text)**。您可以按下列步驟修改教程檔案:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

被添加到第二行的 **[NewLine 方法](../selection/selection_newline)** 會在游標位置插入一個新的行。在第三行的代碼會在字串起始位置插入一個 tab 字元。一個 tab 字元在 JavaScript 中由 "\\t" 表示，在 VBScript 中由 Chr(9) 表示。您同樣能用 VBScript 常數，vbTab，作為一個 tab 字元。

下清單格列出了在 JavaScript 和 VBScript 常用的逸出序列。

#### \[JavaScript\]

|     |     |     |
| --- | --- | --- |
| \\b | \\u0008 | 后退鍵。 |
| \\t | \\u0009 | 水平 tab。 |
| \\n | \\u000a | 新行。 |
| \\f | \\u000c | 換頁。 |
| \\r | \\u000d | 歸位。 |
| \\" | \\u0022 | 雙引號。 |
| \\' | \\u0027 | 單引號。 |
| \\\ | \\u005c | 反斜杠。 |
| \\xXX |  | 由兩個十六進位數指定的含編碼的 Latin-1 字元。 |
| \\uXXXX |  | 由四個十六進位數指定的含編碼的 Unicode 字元。 |

#### ![](../../images/g.gif) 參考:  [JScript \ 特殊字元 (Microsoft MSDN Library)](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Lexical_grammar\#%E5%AD%97%E4%B8%B2)

#### \[VBScript\]

|     |     |     |
| --- | --- | --- |
| vbCr | Chr(13) | 歸位。 |
| vbCrLf | Chr(13) & Chr(10) | 歸位 \+ 新行組合。 |
| vbFormFeed | Chr(12) | 換頁。 |
| vbLf | Chr(10) | 新行。 |
| vbNewLine | Chr(13) & Chr(10) or Chr(10) | 特定平臺的新行字元。相當于 Windows 中的 vbCrLf。 |
| vbTab | Chr(9) | 水平 tab。 |
| vbVerticalTab | Chr(11) | 垂直 tab。 |

#### ![](../../images/g.gif) 參考:  [VBScript \ 字串常數 (Microsoft MSDN Library)](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/scripting-articles/hh277t8e(v=vs.84))

## 提示

行尾端以一個 \\r (CR) 和一個 \\n (LF) 的組合結尾。CR 和 LF 使用不同方式。例如，如果您寫:

document.selection.Text = "\\n";

插入的僅僅是歸位符 (LF)，而不是 Windows 行尾端的慣例。當您在 EmEditor 中按歸位鍵時，EmEditor 會插入該行所用的行尾端方式 (僅 CR，僅 LF，或 CR+LF) 。如果您想要在按歸位鍵時與在 EmEditor 中有相同的行為，我們建議您用
**[NewLine 方法](../selection/selection_newline)**
或 **[writeln 方法](../document/document_writeln)**。

## 下一主題: