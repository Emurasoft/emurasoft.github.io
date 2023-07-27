# CharLeft 方法 (Selection ��H)

把游標向左移動指定的字元數。

## 

### \[JavaScript\]

```
document.selection.CharLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.CharLeft [ bExtend [, nCount ] ]
```

## 參數

_bExtend_

可選項。指定是否折疊被移動的文字。預設的值為 false，并且所移動的文字被折疊。

_nCount_

可選項。指定向左移動的字元數。預設值是 1。如果指定的是負數，該方法與 [CharRight \
方法](selection_charright) 的行為相同。如果指定的是 0，會向左移動 1 個字元。

## 版本

支持 EmEditor 4.00 或之後的版本。
