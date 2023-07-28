# Numbering Method (Document Object)

Inserts numbering at the cursor position or vertical selection.

## 

### \[JavaScript\]

```
document.Numbering( strFirst, strInc, nMaxLines [, nFlags ] );
```

### \[VBScript\]

```
document.Numbering strFirst, strInc, nMaxLines [, nFlags ]
```

## Parameters

_strFirst_

Specifies an initial value or character to insert at the first line. This text may include non-number prefix and/or suffix unless the **eeNumOther** is specified for the _nFlags_ parameter.

_strInc_

Specifies an increment in the decimal notation. This is the change in value between the first line and the second line.

_nMaxLines_

Specifies the number of lines in the decimal notation.

_nFlags_

You can specify a combination of the following values. If 0 is specified or omitted, this method inserts numbering in decimal notation.

| Value | Meaning |
| --- | --- |
| eeNumCapitalLetters | Inserts hexadecimal values in capital letters. |
| eeNumSkipEmptyLines | Numbering will continue after empty lines, without numbering the empty lines during vertical selection mode or multiple selection mode. |
| eeNumRestartNumEmpty | Numbering will restart from the first value after empty lines during vertical selection mode or multiple selection mode. |
| eeNumRestartNumDiscontinuous | Numbering will restart from the first value at discontinuous lines during multiple selection mode. |
| eeNumHexadecimal | Inserts numbers in hexadecimal notation. |
| eeNumOctal | Inserts numbers in octal notation. |
| eeNumBinary | Inserts numbers in binary notation. |
| eeNumOther | Inserts characters instead of numbers. Starting with the number specified in <br>the _pszFirst_ parameter, this option inserts sequential characters using the <br>increment of the Unicode value specified in the _pszInc_ parameter. Only one <br>character can be inserted at each line. |

## Version

Supported on Version 19.1 or later.
