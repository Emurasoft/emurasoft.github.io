# AddFind 方法 (Filters 集合)

添加一個要搜索的項目。

## 

### \[JavaScript\]

```
list.AddFind( strFind, nFlags, nExFlags );
```

### \[VBScript\]

```
list.AddFind( strFind, nFlags, nExFlags )
```

## 參數

_strFind_

指定要搜索的字串。

_nFlags_

指定一個以下值的組合。

|     |     |
| --- | --- |
| eeFindLogicalOr | 如果篩選有多個級別，請指定與上一級的邏輯分離（邏輯 OR）。 |
| eeFindNegative | 顯示「篩選」工具列，並排除與指定字串符合的行。 |
| eeFindReplaceCase | 符合大小寫。 |
| eeFindReplaceEscSeq | 使用逸出數列。不能與 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整個單字需符合。 |
| eeFindReplaceRegExp | 使用規則運算式搜索字串。不能與 eeFindReplaceEscSeq 合用。 |
| eeFindWholeString | 符合整個字串。 |

_nExFlags_

指定一個以下值的組合:

|     |     |
| --- | --- |
| eeExFindBookmarkedOnly | 僅符合書籤行。此標志不能與 eeExFindUnbookmarkedOnly 合用。 |
| eeExFindCrLf | 符合換行符號為 CR 和 LF 的行。此標志不能與 eeExFindMatchNL 合用。 |
| eeExFindCrOnly | 符合換行符號僅是 CR 的行。此標志必須與 eeExFindMatchNL 合用。 |
| eeExFindFuzzy | 使用模糊比對。 |
| eeExFindLfOnly | 符合換行符號僅是 LF 的行。此標志必須與 eeExFindMatchNL 合用。 |
| eeExFindLinkFile | 指定 _strFind_ 是連結檔案的檔案路徑，該連結檔案包含多個用換行符分隔的搜索字串。如果一行中包含 Tab，則搜索字串是第一個不包含 Tab 的字串。 _strFind_ 可以是 EmEditor 安裝路徑的相對路徑。它可以包含環境變數，例如 %USERPROFILE%。要指定正在運行的巨集資料夾中的檔案，請使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindMatchNL | 符合指定的換行符號。此標志應與 eeExFindCrLf，eeExFindCrOnly，eeExFindLfOnly，和/或 eeExFindNLOthers 合用。 |
| eeExFindNLOthers | 符合沒有換行符號的行。這些行包括檔案的最後一行和很長的行，這些行繼續到下一行而沒有換行符號。此標志必須與 eeExFindMatchNL 合用。 |
| eeExFindNumberRange | 符合 [數字範圍運算式](../../howto/search/number_range_syntax)。此標志不能與 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindUnbookmarkedOnly | 僅符合未標示為書籤的行。此標志不能與 eeExFindBookmarkedOnly 合用。 |
| eeExFilterBegin | 指定一個開始篩選。此標志不能與 eeExFilterEnd 合用。 |
| eeExFilterEnd | 指定一個結束篩選。此標志不能與 eeExFilterBegin 合用。 |

## 版本

支持 EmEditor Professional 19.9 或之後的版本。
