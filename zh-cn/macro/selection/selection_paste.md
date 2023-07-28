# Paste 方法 (Selection 对象)

在光标处插入剪贴板内容。

## 

### \[JavaScript\]

```
document.selection.Paste( nFlags );
```

### \[VBScript\]

```
document.selection.Paste nFlags
```

## 参数

_nFlags_

指定一个下列值的组合:

|     |     |
| --- | --- |
| eeCopyUnicode | 粘贴为 Unicode（默认）。 |
| eeCopyQuotes | 粘贴为引用文本。 |
| eeCopyNL | 用新行粘贴。 |
| eeCopySystemDefault | 粘贴为 [系统默认编码](../../glossary/systemdefaultencoding)。 |

## 版本

支持 EmEditor 4.00 或之后的版本。
