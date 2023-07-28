# Item 属性 (Documents 集合)

为指定索引的文档检索文档对象。

## 

### \[JavaScript\]

```
doc = editor.Documents.Item( Index );
```

### \[VBScript\]

```
doc = editor.Documents.Item( Index )
```

## 参数

_Index_

指定以 1 为基准的整数为文档的索引。

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

支持 EmEditor 5.00 或之后的版本。
