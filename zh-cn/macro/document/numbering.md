# Numbering 方法 (Document 对象)

在鼠标位置或垂直选择处，插入编号。

## 

### \[JavaScript\]

```
editor.Numbering( strFirst, strInc, nMaxLines [, nFlags ] );
```

### \[VBScript\]

```
editor.Numbering strFirst, strInc, nMaxLines [, nFlags ]
```

## 参数

_strFirst_

指定要在第一行插入的初始值或字符。除非为 _nFlags_ 参数指定了 **eeNumOther**，否则此文本可能包含非数字前缀和/或后缀。

_strInc_

指定十进制形式的增量。这是第一行和第二行之间的值的变化。

_nMaxLines_

指定十进制形式的行数。

_nFlags_

你可以指定以下值的组合。如果指定或省略0，则此方法会以十进制形式插入数字。

| 值 | 含义 |
| --- | --- |
| eeNumCapitalLetters | 以大写字母插入十六进制值。 |
| eeNumSkipEmptyLines | 在空行后继续编号，而不会在垂直选择模式或多选区模式期间对空行进行编号。 |
| eeNumRestartNumEmpty | 在垂直选择模式或多选区模式下，编号在空行后将从第一个值重新开始。 |
| eeNumRestartNumDiscontinuous | 在多选区模式下，编号将在不连续的行处从第一个值重新开始。 |
| eeNumHexadecimal | 以十六进制形式插入数字。 |
| eeNumOctal | 以八进制形式插入数字。 |
| eeNumBinary | 以二进制形式插入数字。 |
| eeNumOther | 插入字符而不是数字。从 _pszFirst_ 参数中指定的数字开始，此选项插入用在 _pszInc_ 参数中指定的 Unicode 值的增量的连续字符。每行只能插入一个字符。 |

## 版本

支持 EmEditor Professional v19.1 或之后的版本。
