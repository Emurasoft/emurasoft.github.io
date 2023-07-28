# Item 屬性 (Documents 集合)

為指定索引的文檔檢索文檔對象。

## 

### \[JavaScript\]

```
doc = editor.Documents.Item( Index );
```

### \[VBScript\]

```
doc = editor.Documents.Item( Index )
```

## 參數

_Index_

指定以 1 為基準的整數為文檔的索引。

## 示例

### \[JavaScript\]

```
alert( "Full Name for the first document: " + editor.Documents.Item(1).FullName );
```

### \[VBScript\]

```
alert "Full Name for the first document: " & editor.Documents.Item(1).FullName
```

## 版本

支持 EmEditor 5.00 或之後的版本。
