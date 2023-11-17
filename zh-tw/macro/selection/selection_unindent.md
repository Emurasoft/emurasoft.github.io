# UnIndent 方法 (Selection 對象)

按指定的縮排等級數從被選取的文字中刪除縮排。

## 

### \[JavaScript\]

```
document.selection.UnIndent( [ nCount ] );
```

### \[VBScript\]

```
document.selection.UnIndent [ nCount ]
```

## 參數

_nCount_

可選項。指定縮排等級數。預設值是 1。如果指定的是負數，該方法與 [**Indent**方法](selection_indent) 的行為相同。如果指定值為 0，該方法的行為與指定值為 1 時的行為相同。

## 版本

支持 EmEditor 4.00 或之後的版本。
