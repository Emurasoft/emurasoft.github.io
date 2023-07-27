# AddReplace 方法 (Filters ���X)

添加一個要取代的項目。

## 

### \[JavaScript\]

```
list.AddReplace( strFind, strReplace, nFlags, nExFlags );
```

### \[VBScript\]

```
list.AddReplace( strFind, strReplace, nFlags, nExFlags )
```

## 參數

_strFind_

指定要搜索的字串。

_strReplace_

指定一個要取代為的字串。

_nFlags_

指定一個以下值的組合。

|     |     |
| --- | --- |
| eeFindReplaceCase | 匹配大小寫。 |
| eeFindReplaceEscSeq | 使用逸出數列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整個單字需符合。 |
| eeFindReplaceRegExp | 使用規則運算式搜索字串。不能與 eeFindReplaceEscSeq 合用。 |

_nExFlags_

指定一個以下值的組合:

|     |     |
| --- | --- |
| eeExFindLinkFile | 指定 _strFind_ 是連結檔案的檔案路徑，該連結檔案包含多個用換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab 的字串，取代字串則是第二個字串。 _strFind_ 可以是 EmEditor 安裝路徑的相對路徑。它可以包含環境變數，例如 %USERPROFILE%。要指定正在運行的巨集資料夾中的檔案，請使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindFuzzy | 使用模糊比對。 |

## 版本

支持 EmEditor Professional 19.9 或之後的版本。
