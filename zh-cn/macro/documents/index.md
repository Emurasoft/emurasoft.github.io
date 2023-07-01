# Documents 集合

Documents 集合在一个框架窗口中提供文档对象的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](documents_count)** | 检索文档的数目。 |
| **[Item](documents_item)** | 为指定索引的文档检索文档对象。 |

## 示例

#### \[JavaScript\]

docs = new Enumerator( editor.Documents );

for( ; !docs.atEnd(); docs.moveNext() ){

doc = docs.item();

alert( doc.Name );

}

#### \[VBScript\]

For Each doc In editor.Documents

alert doc.FullName

Next

## 版本

支持 EmEditor 5.00 或之后的版本。


```{toctree}
:maxdepth: 1
documents_count
documents_item
```
