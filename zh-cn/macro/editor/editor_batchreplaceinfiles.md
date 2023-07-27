# BatchReplaceInFiles 方法 (Editor ����)

在多个文件中替换多个字符串。

## 

### \[JavaScript\]

```
nFound = editor.BatchReplaceInFiles( filters, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ] );
```

### \[VBScript\]

```
nFound = editor.BatchReplaceInFiles( filters, strPath, nFlags, [ nEncoding, [ strFilesToIgnore, [ strBackupPath, [ nExFlags, [ nLimit ] ] ] ] ] )
```

## 参数

_filters_

指定包含搜索字符串和标志的 [Filters 集合](../filters/index)。

_strPath_

指定要搜索的路径。它可以包括通配符，例如\\* 以及 ?。

_nFlags_

指定一个下列值的组合。

|     |     |
| --- | --- |
| eeFindRecursive | 在指定路径的子文件夹中搜索。 |
| eeFindReplaceIgnoreFiles | 忽略由 _strFilesToIgnore_ 指定的文件或文件夹。 |
| eeOpenDetectAll | 检测所有编码。 |
| eeOpenDetectCharset | 检测 HTML/XML 字符集。 |
| eeOpenDetectUnicode | 检测 Unicode 签名 (BOM)。 |
| eeOpenDetectUTF8 | 检测 UTF-8。 |
| eeReplaceBackup | 保存备份。不能与 eeReplaceKeepOpen 合用。 |
| eeReplaceKeepOpen | 保持修改的文件为打开状态。不能与 eeReplaceBackup 合用。 |

_nEncoding_

从[编码常数](../const/const_encoding) 中选择或指定任何用于 Windows 操作系统的代码页。如果指定 0 或省略，将使用与搜索的文件名关联的配置属性中指定的编码。

_strFilesToIgnore_

如果 _nFlags_ 包括 eeFindReplaceIgnoreFiles，指定要忽略的文件或文件夹名称。它可以包括通配符，例如 \* 和 ?。要指定多个文件，用分号 (;) 来隔开文件。

_strBackupPath_

指定备份文件夹如果 _nFlags_  指定了 eeReplaceBackup。

_nExFlags_

指定下列值的组合。但是，只能指定 eeExFindRegexBoost 和 eeExFindRegexOnigmo 中的一个。如果未指定这两者，则使用默认的正则表达式引擎。

|     |     |
| --- | --- |
| eeExFindMulti | 执行多项替换全部。如果未指定，则执行批处理替换全部。详情请参阅 [批处理替换全部和多项替换全部之间的区别](../../howto/search/batch_vs_bulk)。 |
| eeExFindRegexBoost | 使用 Boost.Regex 作为正则表达式引擎。 |
| eeExFindRegexOnigmo | 使用 Onigmo 作为正则表达式引擎。 |

_nLimit_

当匹配数达到此数字时，EmEditor 将停止搜索文件。 如果指定 0，则 EmEditor 不会停止搜索文件。

## 返回值

返回值是在所有搜索的文件中替换的字符串总数。

## 备注

除非 _nFlags_  指定 eeReplaceKeepOpen，否则无法撤消此操作。
建议将 eeReplaceBackup 指定为 _nFlags_  并保存备份。
如果备份文件夹中存在相同的文件名，则新备份将覆盖旧文件。

## 版本

支持 EmEditor Professional 20.0 或之后的版本。
