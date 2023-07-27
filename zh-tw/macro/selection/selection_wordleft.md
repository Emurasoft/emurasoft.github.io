# WordLeft 方法 (Selection ��H)

把游標向左移指定的單字數。

## 

### \[JavaScript\]

```
document.selection.WordLeft( [ bExtend [, nCount ] ] );
```

### \[VBScript\]

```
document.selection.WordLeft [ bExtend [, nCount ] ]
```

## 參數

_bExtend_

可選項。指定是否折疊被移動的文字。預設的值為 false，并且所移動的文字被折疊。

_nCount_

可選項。指定向左移的單字數。預設值是 1。如果指定的是負數，該方法與 [WordRight \
方法](selection_wordright) 的行為相同。如果指定值為 0，該方法的行為與指定值為 1 時的行為相同。

## 版本

支持 EmEditor 4.00 或之後的版本。
