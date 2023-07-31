# Documents 集合

Documents 集合在一個框架視窗中提供文檔對象的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](documents_count)** | 檢索文檔的數目。 |
| **[Item](documents_item)** | 為指定索引的文檔檢索文檔對象。 |

## 示例

### \[JavaScript\]

```
docs = new Enumerator( editor.Documents );
for( ; !docs.atEnd(); docs.moveNext() ){
doc = docs.item();
alert( doc.Name );
}
```

### \[VBScript\]

```
For Each doc In editor.Documents
alert doc.FullName
Next
```

## 版本

支持 EmEditor 5.00 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
documents_count
documents_item
```
