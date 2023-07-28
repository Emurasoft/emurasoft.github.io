# EndOfLine 方法 (Selection 對象)

把游標移到目前的行的尾端。

## 

### \[JavaScript\]

```
document.selection.EndOfLine( [ bExtend [, nFlags ] ] );
```

### \[VBScript\]

```
document.selection.EndOfLine [ bExtend [, nFlags ] ]
```

## 參數

_bExtend_

可選項。指定是否折疊被移動的文字。預設的值為 false，并且所移動的文字被折疊。

_nFlags_

可選項。指定一個下列值得組合:

|     |     |
| --- | --- |
| eeLineView | 指定顯示行。 |
| eeLineLogical | 指定邏輯行。 |

## 版本

支持 EmEditor 4.00 或之後的版本。
