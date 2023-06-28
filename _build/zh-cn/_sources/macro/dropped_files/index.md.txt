# DroppedFiles 集合

DroppedFiles 集合在一个框架窗口中提供拖放的文件名称的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索被拖放的文件的数目。 |
| **[Item](item)** | 检索指定索引下的被拖放的文件名。 |

## 示例

#### \[JavaScript\]

files = new Enumerator( DroppedFiles );

for( ; !files.atEnd(); files.moveNext() ){

alert( files.item() );

}

#### \[VBScript\]

For Each str In DroppedFiles

alert str

Next

## 版本

支持 EmEditor 8.00 或之后的版本。

```{toctree}
:maxdepth: 1
count
item
```
