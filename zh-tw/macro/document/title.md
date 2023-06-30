# Title 屬性 (Document ��H)

檢索或設定文檔標題。標題可以包含由換行符符號分隔的長標題和短標題（\\n 或 Chr(10)）。

#### \[JavaScript\]

_strTitle_ = document. **Title**;document. **Title** = _strTitle_;

#### \[VBScript\]

_strTitle_ = document. **Title** document. **Title** = _strTitle_

## 範例

#### \[JavaScript\]

document.Title = "This is a long title.\\nShort title";

#### \[VBScript\]

document.Title = "This is a long title." & Chr(10) & "Short title"

## 版本

支持 EmEditor Professional v21.8 或之後的版本。