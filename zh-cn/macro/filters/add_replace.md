# AddReplace 方法 (Filters 集合)

添加一个要替换的项目。

## 

### \[JavaScript\]

```
list.AddReplace( strFind, strReplace, nFlags, nExFlags );
```

### \[VBScript\]

```
list.AddReplace( strFind, strReplace, nFlags, nExFlags )
```

## 参数

_strFind_

指定要搜索的字符串。

_strReplace_

指定一个要替换为的字符串。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindReplaceCase | 大小写需符合。 |
| eeFindReplaceEscSeq | 使用转义序列。不能与 eeFindReplaceRegExp 合用。 |
| eeFindReplaceOnlyWord | 整个单词需匹配。 |
| eeFindReplaceRegExp | 使用正则表达式搜索字符串。不能与 eeFindReplaceEscSeq 合用。 |

_nExFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeExFindLinkFile | 指定 _strFind_ 是链接文件的文件路径，该链接文件包含多个用换行符分隔的搜索字符串。如果一行中包含制表符，则搜索字符串是第一个不包含制表符的字符串，替换字符串则是第二个字符串。 _strFind_ 可以是 EmEditor 安装路径的相对路径。它可以包含环境变量，例如 %USERPROFILE%。要指定正在运行的宏文件夹中的文件，请使用以下形式：<br>ScriptFullName.substr( 0, ScriptFullName.lastIndexOf( "\\\\" ) + 1 ) + "LinkFile.txt" |
| eeExFindNumberRange | 匹配 [数字范围表达式](../../howto/search/number_range_syntax)。此标志不能与 eeFindReplaceEscSeq 或 eeFindReplaceRegExp 合用。 |
| eeExFindFuzzy | 使用模糊匹配。 |

## 版本

支持 EmEditor Professional 19.9 或之后的版本。
