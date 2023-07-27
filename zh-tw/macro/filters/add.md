# Add 方法 (Filters ���X)

添加一個項目。

## 

### \[JavaScript\]

```
list.Add( strFilter, bEnabled, iColumn, nFlags, xBegin, xEnd, strReplace, nExFlags );
```

### \[VBScript\]

```
list.Add strFilter, bEnabled, iColumn, nFlags, xBegin, xEnd, strReplace, nExFlags
```

## 參數

_strFilter_

指定一個要搜索的字串。

_bEnabled_

指定是否要啟用這個篩選。

_iColumn_

指定你想要搜索的以 1 為基準的文字的列的索引；如果你要搜索整行，可以指定 0 ；如果你要用字元數把開始以及結尾的文字指定為 _xBegin_ 和 _xEnd_，可以指定 -1。

_nFlags_

指定一個下列值的組合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 指定一個邏輯或運算 (logical OR) 到之前的層級上在多層級篩選的情況下。 |
| eeFindNegative | 顯示篩選工具列并排除與指定字串符合的行。 |
| eeFindReplaceCase | 大小寫需符合。 |
| eeFindReplaceEscSeq | 使用逸出序列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整個單字需符合。 |
| eeFindReplaceRegExp | 使用規則運算式搜索字串。不能與 eeFindReplaceEscSeq 合用。 |
| eeFindWholeString | 符合整個字串。 |

_xBegin_

指定你想要搜索的文字的起始欄的索引（邏輯字元數）；指定 0 如果你想要把文字的最後一部分作為 _xEnd_。要使這個欄位有效， _iColumn_ 值必須是 -1。

_xEnd_

指定你想要搜索的文字的末尾欄的索引（邏輯字元數）；指定 0 如果你想要搜索所有剩下的文字。要使這個欄位有效， _iColumn_ 值必須是 -1。

_strFilter_

指定要取代為的字串。

_nExFlags_

指定一個以下值的組合:

|     |     |
| --- | --- |
| eeExFindLinkFile | 指定 _strFilter_ 是連結檔案的檔案路徑，該連結檔案包含多個用換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab 的字串。 _strFilter_ 可以是 EmEditor 安裝路徑的相對路徑。它可以包含環境變數，例如 %USERPROFILE%。要指定正在運行的巨集資料夾中的檔案，請使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindFuzzy | 使用模糊比對。 |

## 版本

支持 EmEditor 16.0 或之後的版本。
