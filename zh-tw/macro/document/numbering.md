# Numbering 方法 (Document 對象)

在游標位置或垂直選擇處，插入編號。

## 

### \[JavaScript\]

```
editor.Numbering( strFirst, strInc, nMaxLines [, nFlags ] );
```

### \[VBScript\]

```
editor.Numbering strFirst, strInc, nMaxLines [, nFlags ]
```

## 參數

_strFirst_

指定要在第一行插入的初始值或字元。除非為 _nFlags_ 參數指定了eeNumOther，否則此文字可包含非數字首碼和/或尾碼。

_strInc_

指定十進位形式的增量。這是第一行和第二行之間的值的變化。

_nMaxLines_

指定十進位形式的行數。

_nFlags_

你可以指定以下值的組合。如果指定或省略0，則此方法會以十進位形式插入數字。

| 值 | 含義 |
| --- | --- |
| eeNumCapitalLetters | 以大寫字母插入十六進位值。 |
| eeNumSkipEmptyLines | 在空行后繼續編號，而不會在垂直選擇模式或多選區模式期間對空行進行編號。 |
| eeNumRestartNumEmpty | 在垂直選擇模式或多選區模式下，編號在空行后將從第一個值重新開始。 |
| eeNumRestartNumDiscontinuous | 在多選區模式下，編號將在不連續的行處從第一個值重新開始。 |
| eeNumHexadecimal | 以十六進位形式插入數字。 |
| eeNumOctal | 以八進位形式插入數字。 |
| eeNumBinary | 以二進位形式插入數字。 |
| eeNumOther | 插入字元而不是數字。從 _pszFirst_ 參數中指定的數字開始，此選項插入用在 _pszInc_ 參數中指定的 Unicode 值的增量的連續字元。每行只能插入一個字元。 |

## 版本

支持 EmEditor Professional v19.1 或之後的版本。
