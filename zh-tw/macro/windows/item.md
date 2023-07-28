# Item 屬性 (Windows 集合)

為指定索引的視窗檢索視窗對象。

## 

### \[JavaScript\]

```
wnd = shell.windows.Item( Index );
```

### \[VBScript\]

```
wnd = shell.windows.Item( Index )
```

## 參數

_Index_

用以 1 為基準的整數指定視窗的索引。

## 示例

### \[JavaScript\]

```
alert( "Name of the first window: " + shell.windows.Item(1).Caption );
```

### \[VBScript\]

```
alert "Name of the first window: " + shell.windows.Item(1).Caption
```

## 版本

支持 EmEditor 7.00 或之後的版本。
