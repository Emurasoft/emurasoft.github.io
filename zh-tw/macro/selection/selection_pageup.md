# PageUp 方法 (Selection ��H)

在文檔中，把游標上移指定的頁數。

#### \[JavaScript\]

document.selection. **PageUp**( \[ _bExtend_ \[, _nCount_ \] \] );

#### \[VBScript\]

document.selection. **PageUp** \[ _bExtend_ \[, _nCount_ \] \]

## 參數

_bExtend_

可選項。指定是否折疊被移動的文字。預設的值為 false，并且所移動的文字被折疊。

_nCount_

可選項。指定上移的頁數。預設值是 1。如果指定的是負數，該方法與 [**PageDown** \
方法](selection_pagedown) 相同。如果指定值為 0，該方法的行為與指定值為 1 時的行為相同。

## 版本

支持 EmEditor 4.00 或之後的版本。