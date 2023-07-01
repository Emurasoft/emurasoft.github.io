# Title 属性 (Document ����)

检索或设置文档标题。标题可以包含由换行符分隔的长标题和短标题（\\n 或 Chr(10)）。

#### \[JavaScript\]

_strTitle_ = document. **Title**;document. **Title** = _strTitle_;

#### \[VBScript\]

_strTitle_ = document. **Title** document. **Title** = _strTitle_

## 示例

#### \[JavaScript\]

document.Title = "This is a long title.\\nShort title";

#### \[VBScript\]

document.Title = "This is a long title." & Chr(10) & "Short title"

## 版本

支持 EmEditor Professional v21.8 或之后的版本。
